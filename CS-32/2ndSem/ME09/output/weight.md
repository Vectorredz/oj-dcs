## Additional Questions

---

#### 1. [2.5 pts] Create a rough scheme that lets you find most complex roots (within the grid range specified) using Newton's method. That is, how are you able to find $\texttt{roots}$ without using any of Numpy's methods such as $\texttt{np.root()}$?

Notice that $\texttt{np.root()}$ relies on algebraic methods to find the roots of a certain polynomial. 

As a rough scheme in finding roots using the iterative method, **Newton's method**:

1. Define the 2D grid of complex number as:

 $$X_{\text{newton}} = \text{re}[:, \text{np.newaxis}] + i \cdot \text{im}[\text{np.newaxis}, :]$$

with a specified grid range:

$x_{\text{range}} = [-2, 2]$,
$y_{\text{range}} = [-2, 2]$

1. Let function $f(r)$ takes $r$ as the root. Define the $f'(r)$ be the first derivative of the function. 

2. Given that the grid is a 2D array composing of possible $r_0$ roots starting points, we can iterate through the 2D array and apply the newton's method formula.


Hence, 

$$
r_1 = r_0 - \frac{f(r_0)}{f'(r_0)}
$$

In general, 

$$
r_0 = X_{\text{newton}}[i][j]
$$

Where, the $i$ refers to the current $re$ at that row and $j$ refers to the $im$ component of the complex root.

1. After converging to a complex root at a certain starting point chosen from $X_{\text{newton[i][j]}}$ we store the root into a `set()` to avoid storing **repeated roots** and apply `list()` if we want to print it. 
2. Iterate over the grid and take another value from $X_{\text{newton[i][j]}}$ rowwise and apply the newton's method all over again. 
3. Repeat until all the elements from the grid is covered.

#### 2. [2.5 pts] Relate this with how you would be able to find every *singular* real root given an arbitrary function where the roots are inside the interval $[a,b]$ where $a,b \in \mathbb{R}$ and $a<b$. A rough sketch of the solution suffices.

Similarly, we can apply the same concept from the complex roots. However, since we are now tasked to find every singular real root then, we will only work with a 1D array. The 1D array spans from [a,b] where b-a is the size of the array. 
1. We first discretize the intervals by defining the 1D array of real numbers
$$
x_{\text{newton}} = \mathrm{np.linspace}\biggl(a,\, b,\, \mathrm{num} = \bigl(b - a) \times \text{res\_per\_unit}\biggr)
$$
2. Apply the newton's method for each elements from the root

Hence, 

$$
r_1 = r_0 - \frac{f(r_0)}{f'(r_0)}
$$

In general, 

$$
r_0 = x_{\text{newton}}[i]
$$

**Your explanation here:**

#### 3. [5 pts] From your answer in part (2), explain how you would implement $\texttt{FindAllRealRoots(p)}$ where $p$ is a list containing polynomial coefficients with the same convention as above. This function computes **ALL** real roots over $\mathbb{R}$. For multiple roots, you are not required to find the multiplicity apart from returning which roots have a multiplicity greater than 1. You are not required to write a Python program (although you can submit one as your solution); a pseudocode is enough. Where do you think your algorithm would fail to find a solution?