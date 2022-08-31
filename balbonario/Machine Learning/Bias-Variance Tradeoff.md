The *bias-variance tradeoff* refers to a common phenomenon occurring in many statistical models where it is not possible to decrease both the bias and the variance of a model[^bias-variance-definition] by changing the number of parameters of a model.

[^bias-variance-definition]: For definitions of the bias and variance of a model see [[Bias-Variance Decomposition]].

This phenomenon is true in the classical regime where the number of free parameters is less than the number of datapoints, but stops to hold for overparameterized models where the situation reverts with both bias and variance decreasing in what has been called [[Double Descent]].

The crux of that phenomenon is that if there is some kind of strong regularization (which may be implicit in the learning algorithm) then the algorithm will converge to models which perfectly interpolate the training data, while also doing good on test data.
From a mild overparameterization onward, each new parameter is used in a more complicated kind of smoothing of the test data, which may actually fit the test data better.
