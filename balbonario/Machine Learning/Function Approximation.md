The setting of Function Approximation is the following: suppose you are given two spaces $X$ and $Y$, which model respectively the "independent variable" and the "dependent variable" or, more clearly, $X$ is the variable you can observe (such as concentrations of various molecules in blood) and $Y$ is the variable you are interested in predicting (such as the possibility of a stroke to that person).

We assume that the $n$ data samples $\left\{z_i = (x_i, y_i)\right\}_{i=1}^n$ that we have in our concrete problem come from a joint (regular enough) probability distribution $\mathcal{D}$ on $X \times Y$ and we write it as $(x_i, y_i) \sim \mathcal{D} \in \mathcal{P}(X \times Y)$.
The problem is to find a function $f$ in a certain class $\mathcal{F}$[^function-class] that well-approximates the empirical law between $x_i$ and $y_i$ in a way that allows us to suffer the least losses.

In fact, we typically we have an idea of the cost associated with a given misprediction, and we can model this as a [[Loss Function]] $\ell: X \times Y \times Y \rightarrow \mathbb{R}$.
Then we are interested in the minimization of the cost over the whole input distribution, i.e. we are interested in solving the problem
$$\min_{f \in \mathcal{F}}\ \mathbb{E}_{(X, Y) \sim \mathcal{D}}\left[\ell(X, Y, f(X))\right].$$

[^function-class]: In this case the function class $\mathcal{F}$ is used to enforce some regularity conditions or architectural biases on the kind of function that $f$ is allowed to be, e.g. one can force $f$ to be continuous or to be linear or to be written as a convolution in a certain measure space.

We typically need to find a proxy for such a quantity with the data samples that we are given. Usually this proxy quantity is given by [[Empirical Risk Minimization]] with some kind of [[Regularization]], and we can thus write the function to be minimized as
$$\mathcal{L}(f) := \frac1n \sum_{i=1}^n \ell(x_i, y_i, f(x_i)) + \lambda \Omega(f)$$
where $\ell$ and $\Omega: \mathcal{F} \rightarrow \mathbb{R}$ (the *regularization term*) are assumed to be convex functions so that standard [[Convex Optimization]] procedures apply, and it is feasible to find a solution to the minimization problem.
