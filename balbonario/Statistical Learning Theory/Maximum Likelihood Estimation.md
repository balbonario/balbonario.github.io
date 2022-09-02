A general method to derive a loss function when an analytical form for the data-generating probability is known.

Suppose that we have a random sample $y_i$ for $i = 1, \ldots, n$ from a density $\text{Pr}_\theta(y)$ which is indexed by some parameters $\theta$. The log-probability of the observed sample is:
$$\mathcal{L}(\theta) := \sum_{i=1}^n \log \text{Pr}_\theta(y_i).$$

The principle of maximum likelihood assumes that the most reasonable values for $\theta$ are those for which the probability of the observed sample is largest.

## Derived Losses
This principle is at the base of the definition of both [[Mean Squared Error]] and [[Categorical Cross-Entropy]].

Indeed, consider the additive error model $Y = f_\theta(X) + \varepsilon$ where $\varepsilon \sim \mathcal{N}(0, \sigma^2)$. This model is equivalent to maximum likelihood using the conditional likelihood
$$\text{Pr}(Y \mid X, \theta) = \mathcal{N}(f_\theta(X), \sigma^2)$$
whose log-likelihood gives rise to [[Mean Squared Error]].

Consider now what happens for a multinomial likelihood for the regression function $\text{Pr}(G \mid X)$ where $G$ is a categorical output; suppose we have a model $\text{Pr}(G = g_k \mid X = x) = p_{k, \theta}(x)$ for $k = 1, \ldots, K$ for the conditional probability of each class given $X$.
Then the log-likelihood is
$$\mathcal{L}(\theta) = \sum_{i=1}^n \log p_{g_i, \theta}(x_i)$$
which gives rise to [[Categorical Cross-Entropy]] loss.
