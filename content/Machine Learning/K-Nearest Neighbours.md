---
title: "K-Nearest Neighbours"
---

$k$-nearest neighbours is a [[Function Approximation]] algorithm which assumes that the function to approximate is locally constant, and thus approximates the output variable $\hat y$ with a mean of the $k$ nearest neighbours, i.e.
$$\hat y(x) := \frac1k \sum_{i \in N_k(x)} y_i$$
where $N_k(x)$ represents the set of the $k$ neighbours of $x$, and which necessitates of a metric over $X$ to be specified.

The number of effective parameters of the method is $n/k$, where $n$ is the number of datapoints, since the method essentially fits a mean to each grouping of $k$ elements, thus fitting $n/k$ means.
