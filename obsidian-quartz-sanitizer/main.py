from pathlib import Path
import os
import re
import yaml
import string
import random
import subprocess

IN_DIR = Path(r'balbonario')
DEFAULT_DRAFT = False

# --- CHANGE THE ABOVE, NOTHING BELOW THIS LINE ---

OUT_DIR = Path(r'content')

def sanitize_string(s):
    """
    given some string s, make it url-friendly
    """
    # replace spaces with -'s and remove all other url unfriendly chars
    s = re.sub(' ', '-', s)
    s = re.sub('[^0-9a-zA-Z\-\._~]', '', s)
    # dedupe -'s
    s = re.sub('-+', '-', s)
    return s.lower()

def sanitize_link(link, files, verbose=True):
    """
    given some Wikilink in the form [[FILENAME#HEADER|VISIBLE]],
    translate to Markdown Link in the form [VISIBLE](FILENAME#HEADER)
    """
    if verbose:
        print(f'Sanitizling link {link}')
    brace = link.find(']')
    pound = link.find('#')
    pipe = link.find('|')
    end_index = min([elt for elt in [brace, pound, pipe] if elt != -1])
    open_brace_index = 2
    filename_portion = link[open_brace_index:end_index]
    visible_portion = filename_portion
    if pipe != -1:
        visible_portion = link[pipe+1:brace]
    header = ''
    if pound != -1:
        if pipe != -1:
            header = link[pound:pipe]
        else:
            header = link[pound:brace]

    # get relative filepath
    search_filename = sanitize_string(filename_portion)
    rel_link = None
    for file in files:
        if search_filename == file.stem:
            rel_link = file.relative_to(OUT_DIR)

    # build Markdown link from Wikilink components and make all backslashes forward slashes
    sanitized_link = f'[{visible_portion}]' + f'({rel_link}{header})'
    sanitized_link = re.sub('\\\\', '/', sanitized_link)
    return sanitized_link

def escape_re_special_characters(s):
    """
    given some string,
    return a regex that matches that string literal
    """
    for re_special_char in '/\-[]{}()*+?.,^$|#':
        s = re.sub(f'\{re_special_char}', f'\{re_special_char}', s)
    return s

def add_frontmatter(s, old_file_path, default_draft=DEFAULT_DRAFT):
    """
    given some note body s and title of note title,
    return the note body with frontmatter appended

    if default_draft, makes all notes drafts
    """
    title = old_file_path.stem
    lastUpdated = subprocess.run(f"git log -1 --pretty='format:%ci' '{old_file_path}'", capture_output=True, shell=True, check=True).stdout
    lines = s.split('\n')
    newfrontmatter = dict(title=title, lastmod=lastUpdated)
    if default_draft:
        newfrontmatter["draft"] = True
    # If a frontmatter already exists we load it and join the two
    if lines[0].startswith("---"):
        oldfrontmatter = yaml.load(s.split("---\n")[1], Loader=yaml.UnsafeLoader)
        newfrontmatter.update(oldfrontmatter)
        lines = s.split("---\n")[2].split("\n")
    # Now we normalize the frontmatter to make it Hugo-compliant
    # All 'url' tags are renamed to 'website'
    if "url" in newfrontmatter:
        newfrontmatter["website"] = newfrontmatter["url"]
        del newfrontmatter["url"]
    # Also take all colons out of 'title'
    newfrontmatter["title"] = newfrontmatter["title"].replace(":", "").replace("'", "")
    # Now we can add our joined frontmatter on top of it
    lines = [
        "---",
        *yaml.dump(newfrontmatter).split("\n"),
        "---",
    ] + lines
    return '\n'.join(lines)

def sanitize_file_contents(path, files):
    """
    given the path to a note and a list of all Obsidian files,
    edits the note body to make Quartz-compliant
    """
    with open(str(path), "r", encoding='utf-8') as f:
        old_text = f.read()

    with open(str(path), "w", encoding='utf-8') as f:
        links = re.findall('\[\[[^\]]*\]\]', old_text)
        sanitized_text = old_text
        for link in links:
            sanitized_link = sanitize_link(link, files)
            escaped_special_chars_link = escape_re_special_characters(link)
            sanitized_text = re.sub(escaped_special_chars_link, sanitized_link, sanitized_text)

        f.write(sanitized_text)

def sanitize_file_name(path):
    """
    given the path to a note,
    copies the note to the OUT_DIR
    and makes filename Quartz-compliant

    note that two non-colliding notes '@this' and 'this'
    will have url-unfriendly chars such as '@' removed, making them collide.
    in this case one will have a random string appended to its filename to avoid collision
    """
    sanitized_parents = [sanitize_string(str(p.stem)) for p in path.relative_to(IN_DIR).parents]
    sanitized_relpath = OUT_DIR
    for p in sanitized_parents[::-1]:
        sanitized_relpath = sanitized_relpath/p
    new_file_path = sanitized_relpath/(sanitize_string(path.stem) + '.md')
    os.makedirs(new_file_path.parent, exist_ok=True)

    # NOTE: We want to overwrite earlier runs of the script
    # # make sure no two notes collide
    # if os.path.isfile(new_file_path):
    #     new_file_path = new_file_path.parent/(''.join(random.choice(string.ascii_lowercase) for i in range(10)) + new_file_path.suffix)

    with open(str(new_file_path), "w", encoding='utf-8') as f:
        with open(str(path), "r", encoding='utf-8') as f_old:
            old_text = f_old.read()

        frontmattered_text = add_frontmatter(old_text, path)
        f.write(frontmattered_text)


if __name__ == '__main__':
    files = [f for f in IN_DIR.rglob("*") if Path(f).suffix == '.md']
    for file in files:
        sanitize_file_name(file)

    renamed_files = [f for f in OUT_DIR.rglob("*") if Path(f).suffix == '.md']
    for file in renamed_files:
        sanitize_file_contents(file, renamed_files)
