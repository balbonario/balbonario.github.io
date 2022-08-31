---
title: "Linear Regression"
---

Linear regression is a [[Function Approximation]] algorithm which assumes that your function is linear, i.e. $\hat Y = \beta X$ where $X \in \mathbb{R}^{p \times n}, \hat Y \in \mathbb{R}^{m \times n}, \beta \in \mathbb{R}^{m \times p}$, and $\beta$ is the matrix of coefficients to be fit.
The method has $mp$ effective parameters.

In order to fit the data you have to specify a [[Loss Function]].
The common one in this setting is [[Mean Squared Error]] on the data, i.e. we are interested in solving the minimization problem
$$\min_\beta \frac1n \sum_{i \le n} (y_i - \beta x_i)^2$$
from which we can derive the normal equations $X^T (y - X \beta) = 0$ and thus the solution $\beta = (X^T X)^{-1} X^T y$.

One can do the same calculations also in the distributional setting and obtain $\beta = \mathbb{E}\left[XX^T\right]^{-1} \mathbb{E}\left[XY\right]$.
