The ROC (Receiver Operating Characteristic) Curve is defined with respect to a given class and encodes the curve of false positive, true positive when varying a threshold $T$ for a one-versus-rest classifier.

In simpler words, suppose that for a given point $x$ we have a model that outputs the probability that this point belongs to a given class $C$ and denote it by $P(C \mid x)$.
Based on this probability we can define a decision rule by setting a threshold $T$ and saying that $x$ belongs to class $C$ if and only if $P(C \mid x) \ge T$.

Each value of the threshold generates a point given by $(\text{false positive ratio}, \text{true positive ratio})$ which defines a curve.
A good model will have a curve that increases quickly from zero to one.

A metric that compresses the information in the ROC curve into a single scalar is the AUROC or Area Under the ROC curve, which tends towards $1.0$ for the best case and towards $0.5$ for the worst cases.
