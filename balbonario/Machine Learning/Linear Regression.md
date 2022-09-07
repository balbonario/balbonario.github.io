Linear regression is a [[Function Approximation]] algorithm which assumes that your function is linear, i.e. $\hat Y = \beta X$ (and can also have a bias term) where $X \in \mathbb{R}^{p \times n}, \hat Y \in \mathbb{R}^{m \times n}, \beta \in \mathbb{R}^{m \times p}$, and $\beta$ is the matrix of coefficients to be fit.
The method has $mp$ effective parameters.

In order to fit the data you have to specify a [[Loss Function]].
The common one in this setting is [[Mean Squared Error]] on the data, i.e. we are interested in solving the minimization problem
$$\min_\beta \frac1n \sum_{i \le n} (y_i - \beta x_i)^2$$
from which we can derive the normal equations $X^T (y - X \beta) = 0$ and thus the solution $\hat\beta = (X^T X)^{-1} X^T y$, and the predicted values at the training inputs are $\hat y = X \hat \beta$.

One can do the same calculations also in the distributional setting and obtain $\beta = \mathbb{E}\left[XX^T\right]^{-1} \mathbb{E}\left[XY\right]$.

In case where the columns of $X$ are not linearly independent, we have that $X^T X$ is singular and the least squares coefficient $\hat\beta$ are not uniquely defined. One usually adds some amount of regularization to retain the uniqueness of the $\hat\beta$ or drops the collinear columns.

#todo Assuming the real model for the mean is linear, and an unbiased estimate of the variance from data, we can devise tests for the hypothesis that $\beta_j = 0$, i.e. that it is irrelevant to predict the $Y$. (Tibshirani et al, page 45 onwards)
This allows us to talk about [[Model Selection]] for linear models with $F$ statistics.

#todo Gauss-Markov theorem
