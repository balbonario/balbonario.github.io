The *curse of dimensionality* is a phenomenon that makes it more difficult to use machine learning problems in high dimensions due to the need of much more data.

Approximately, if $n$ samples provide good results in a single dimension, then $n^d$ samples are needed to provide good results when the input has $d$ dimensions, *under the assumption that the samples are independently distributed on each dimension*.

Another problem in high dimensions is that euclidean distances loose meaning, since distances between two random points have a peaked distribution due to [[Concentration Inequalities]] of random variables (in this case the random components of the data points).
These render ineffective any approach based on [[K-Nearest Neighbours]] or similarity of the input data.

The curse of dimensionality does not apply to models with strong architectural biases, because they don't have the capacity to fit all possible idiosyncrasies of the data, and thus actually perform better in high dimensions.
