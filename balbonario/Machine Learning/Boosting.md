Boosting is a sequential ensembling method to aggregate different weak models. The idea is to fit models iteratively such that the training of successive models is focused on the most difficult observations to fit up to now, so that the bias of the composite learner is reduced, and thus it is a technique usually used on models with low variance but high bias, such as shallow decision trees.

The various boosting techniques differ on the creation and aggregation of the weak learners during the sequential process, typically updating the weights of the weak learners predictors and the distributional resampling for successive models to put more emphasis on misclassified samples.

![[boosting-schema.svg]]
