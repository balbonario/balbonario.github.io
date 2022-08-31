Stacking is a model ensembling technique that is focused on aggregating heterogeneous weak learners with a meta-model that aggregates the decisions of weak models.

For a practical example, suppose that we have a [[K-Nearest Neighbours]] classifier and a [[Logistic Regression]] to aggregate, and we decide to learn a [[Neural Network]] as meta-model.
Then we will split the learning data in two folds; use the first fold to fit the base learners, and make predictions with those on the second fold of data; finally fit the meta-model on the second fold of data, using the predictions by the weak learners as inputs.
