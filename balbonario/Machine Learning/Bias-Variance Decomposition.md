The Bias-Variance Decomposition is a mathematical decomposition of the distributional error.
For the [[Mean Squared Error]] loss we have that
$$
\begin{align*}
\text{MSE}(x_0) & = \mathbb{E}_\mathcal{D}\left[f(x_0) - \hat y_0\right]^2 \\
& = \mathbb{E}_\mathcal{D}\left[\hat y_0 - \mathbb{E}_\mathcal{D}[\hat y_0]\right]^2 + \left(\mathbb{E}_\mathcal{D}[\hat y_0]^2 - f(x_0)\right)^2 \\
& = \text{Var}_\mathcal{D}(\hat y_0) + \text{Bias}(\hat y_0)^2
\end{align*}
$$
where the bias is the displacement of the mean prediction $\hat y_0$ from the true target $y_0 = f(x_0)$, and the variance is the variance of the prediction.

In the case where we assume that there is noise in our measurement of data we get a third additive term which is called irreducible error or noise.

To get the lowest errors we would like to reduce both the bias and the variance, but it happens that we can't do this so easily, and sometimes not at all.

For a fixed model of the data (e.g. [[Linear Regression]]) we can analytically compute the minimum MSE for different settings of the number of parameters of the fit (i.e. the number of coefficients for linear regression).
If one does this, it can be seen that there is a [[Bias-Variance Tradeoff]], i.e. one has to acquire a bit of variance if we want to decrease the bias and viceversa.
