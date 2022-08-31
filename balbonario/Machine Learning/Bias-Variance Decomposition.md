The Bias-Variance Decomposition is a kind of mathematical decomposition of the distributional error.
For the [[Mean Squared Error]] loss we have that
$$
\begin{align*}
\text{MSE}(x_0) & = \mathbb{E}_\mathcal{D}\left[f(x_0) - \hat y_0\right]^2 \\
& = \mathbb{E}_\mathcal{D}\left[\hat y_0 - \mathbb{E}_\mathcal{D}[\hat y_0]\right]^2 + \left(\mathbb{E}_\mathcal{D}[\hat y_0]^2 - f(x_0)\right)^2 \\
& = \text{Var}_\mathcal{D}(\hat y_0) + \text{Bias}(\hat y_0)^2
\end{align*}
$$
where the bias is the displacement of the mean prediction $\hat y_0$ from the true target $y_0 = f(x_0)$, and the variance is the variance of the prediction.
