---
title: "Function Approximation"
---

The setting of Function Approximation is the following: suppose you are given two spaces $X$ and $Y$, which model respectively the "independent variable" and the "dependent variable" or, more clearly, $X$ is the variable you can observe (such as concentrations of various molecules in blood) and $Y$ is the variable you are interested in predicting (such as the possibility of a stroke to that person).

We assume that the $n$ data samples $\left\{z_i = (x_i, y_i)\right\}_{i=1}^n$ that we have in our concrete problem come from a joint (regular enough) probability distribution $\mathcal{D}$ on $X \times Y$ and we write it as $(x_i, y_i) \sim \mathcal{D} \in \mathcal{P}(X \times Y)$.
The problem is to find a function $f$ in a certain class $\mathcal{F}$[^function-class] that well-approximates the empirical law between $x_i$ and $y_i$, i.e. we would like that
$$f(x) := \mathbb{E}_{(X, Y) \sim \mathcal{D}}\left[Y \mid X = x\right].$$

[^function-class]: In this case the function class $\mathcal{F}$ is used to enforce some regularity conditions or architectural biases on the kind of function that $f$ is allowed to be, e.g. one can force $f$ to be continuous or to be linear or to be written as a convolution in a certain measure space.

In order to find such a function we need to specify a [[Loss Function]] $\mathcal{L}: \mathcal{F} \rightarrow \mathbb{R}$. The loss function is typically assumed to be convex so that standard [[Convex Optimization]] procedures apply, to guarantee good convergence results.
