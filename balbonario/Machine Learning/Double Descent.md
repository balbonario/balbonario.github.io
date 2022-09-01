Double Descent is a phenomenon that occurs for overparameterized models: classical statistics advises that there is a [[Bias-Variance Tradeoff]] when the complexity of the model changes, and that one can lose a bit of bias by trading it with an increase in variance and viceversa.

What is instead observed is that when one moves to overparameterized models (i.e. where the number of effective degrees of freedom is higher than the number of datapoints to fit) things change and in the interpolating regime both bias and variance decrease, to an extent that makes such model usually work better than classical ones.

![[double-descent-curve.png]]

Intuitively, the phenomenon happens because at the interpolation threshold, there is often a *single* choice of a model that fits the data, and thus even small amount of noise in the data samples will make the model vary by quite a bit, providing a real overfit.

When the models are instead overparameterized by a bit, we have a variety of models that completely fit the data, and regularization (which is usually implicit in the learning algorithm) is essential to find one that generalize. When adding some noise in the data, the model doesn't change much, and thus doesn't overfit to the idiosyncrasies in the data.

What validates this view is the fact that by adding the appropriate [[Regularization]], the test error peak at the interpolation threshold vanishes and one gets almost monotonic performance.

#### Deepenings
- [Double Descent: A Mathematical Explanation](https://mlu-explain.github.io/double-descent2/) [(Archived)](https://web.archive.org/web/20220831/https://mlu-explain.github.io/double-descent2/)
- [Optimal Regularization can Mitigate Double Descent](https://arxiv.org/pdf/2003.01897.pdf) [(Archived)](https://web.archive.org/web/20220901/https://arxiv.org/pdf/2003.01897.pdf)
- [Kernel Regression in High Dimensions: Refined Analysis beyond Double Descent](http://proceedings.mlr.press/v130/liu21b/liu21b.pdf) [(Archived)](https://web.archive.org/web/20220901/http://proceedings.mlr.press/v130/liu21b/liu21b.pdf)
- [A Modern Take on the Bias-Variance Tradeoff in Neural Networks](https://arxiv.org/pdf/1810.08591.pdf) [(Archived)](https://web.archive.org/web/20220901/https://arxiv.org/pdf/1810.08591.pdf)
