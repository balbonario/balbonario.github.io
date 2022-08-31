Bagging is a set of model ensembling methods where multiple models of the same learner type are built in parallel over different random variations and their predictions aggregated together by averaging or majority vote.

Bagging procedures are based on [[Bootstrapping]] theory, and exploit variations in randomness in the data samples and randomness in the model construction.
In the case of random forests for example, randomness is in the sequential choices of the features to split the dataset.

Averaging the predictions of multiple weak learners doesn't change the average answer but reduces the variances of the learners if the data subsamples can be considered independent (i.e. if their size with respect to the whole dataset is small as not to have too much overlap).
