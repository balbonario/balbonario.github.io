---
title: "Mean Squared Error"
---

The mean squared error is a [[Loss Function]] typically used in classical [[Function Approximation]].
Given $n$ datapoints $(x_i, y_i)$ and relative predictions made by a learning algorithm $\hat y_i = f(x_i)$, the loss function is defined as:
$$\mathcal{L}(f) := \frac1n \sum_{i = 1}^n \left(y_i - f(x_i)\right)^2.$$

It has the benefit of being differentiable giving linear equations to be solved, which makes for easy analytical solutions of the methods that use it.
Moreover, it is the form of [[Maximum Likelihood Estimation]] when one assumes that the real data-generating model is contained in the class $\mathcal{F}$ one is optimizing over, and that measurement errors in the $y_i$ are distributed according to a normal gaussian, i.e. under the assumption that $\exists f \in \mathcal{F} \quad y_i = f(x_i) + \varepsilon_i$ with $\varepsilon_i \sim \mathcal{N}(0, 1)$.
