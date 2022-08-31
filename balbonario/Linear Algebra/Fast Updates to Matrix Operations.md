Given a matrix operation $h$ and a fixed matrix $A$ there are in certain cases better ways to compute $h(A + uv^T)$ from $h(A)$ than to recompute it. This formulas allow for faster online algorithms and are collected in this page.

## Sherman-Morrison Formula
The formula allows to compute the inverse of the sum of an invertible matrix $A$ and the outer product $uv^T$ of two vectors $u, v$.

> [!LEMMA] Sherman-Morrison
> Suppose $A \in \mathbb{R}^{n \times n}$ is an invertible square matrix and $u, v \in \mathbb{R}^n$ are column vectors.
> Then $A + uv^T$ is invertible if and only if $1 + v^T A^{-1} u \neq 0$, and in this case it holds:
> $$(A + uv^T)^{-1} = A^{-1} - \frac{A^{-1} uv^T A^{-1}}{1 + v^T A^{-1} u}.$$

A generalization of this identity for matricial updates is the following.
> [!LEMMA] Woodbury Identity
> Given a square invertible $n \times n$ matrix $A$, two $n \times k$ matrices $U, V$ and an invertible $k \times k$ matrix $W$ we have the identity
> $$(A + U W V^T)^{-1} = A^{-1} - A^{-1} U \left(W^{-1} + V^T A^{-1} U\right)^{-1} V^T A^{-1}.$$

## Matrix Determinant Lemma
The formula allows to compute the determinant of a sum of an invertible matrix $A$ and the outer product of two vectors $uv^T$.

> [!LEMMA] Matrix Determinant Lemma
> Let $A$ be an invertible square matrix and $u, v$ be column vectors. Then it holds:
> $$\text{det}(A + uv^T) = (1 + v^T A^{-1} u)\ \text{det}(A).$$
> 
> In the case where we have $U, V$ as two $n \times m$ matrices and $W$ an additional $m \times m$ invertible matrix we have the identity:
> $$\text{det}(A + UWV^T) = \text{det}(W^{-1} + V^T A^{-1} U)\ \text{det}(W)\ \text{det}(A).$$
