The book starts its discussion of vectors by mentioning numbers drawn
from a <span>**field.**</span>

<span>Field</span> A field is a set $K$ of elements that satisfy
<span>*field axioms*</span>. Essentially these are that

-   addition and multiplication are defined and are associative,
    commutative, and distributive.

-   There is a unit element in $K$

-   Every element in $K$ has an inverse in $K$

Example fields are $\mathbb{R}, \mathbb{Q}, \text{ and } \mathbb{C}$.
Note $\mathbb{Z}$ is not a field because of the inverse requirement.

Consider $n$ values $w_i$ drawn from some field.The ordered collection
of these points is referred to as a <span>**vector.**</span>

The word vector was first used in conjunction with 3-D space. Vectors
are obviously related to a <span>**point**</span> but has an essential
geometric meaning.

Think of the vector $v$ as an arrow pointing from the origin to the
point $p$. Thus vectors have both magnitude and direction. Obviously the
order of the elements of $v$ matter.

We will always write a vector as a column vector.

<span>Vectors</span>

$v_1 = \begin{bmatrix} 2\\-5\end{bmatrix}$,
$v_2=\begin{bmatrix}7\\9\end{bmatrix}$,
$v_3=\begin{bmatrix}3\\4\\5\end{bmatrix}$.

What the book refers to as row vectors we, we will write as the
<span>**transpose**</span> of a column vector.
$$v_4 = v_3^T=\begin{bmatrix}3&4&5\end{bmatrix}$$

The <span>**elements**</span> of the vector are known as
<span>**scalars.**</span>

The <span>**dimension**</span> of a vector is the number of elements in
the vector. If the elements of the vector come from $\mathbb{R}$, we
would indicate the <span>**n-space**</span> of the vector as
$\mathbb{R}^n$.

Vectors are equal when every corresponding elements of the vectors are
equal. The ith element in vector $a$ corresponds to the ith element in
vector $b$.

Operations on Vectors {#operations-on-vectors .unnumbered}
=====================

-   Vector addition is defined by adding point by point the elements of
    the vectors. Conceptually, this is equivalent to adding the vectors
    tip to base.

    <span>Vector Addition \#1</span> Let
    $\vec{a} = \begin{bmatrix}2\\-4\end{bmatrix}$ and
    $\vec{b} = \begin{bmatrix}1\\3\end{bmatrix}$. Then
    $\vec{a+b}=\begin{bmatrix}3\\-1\end{bmatrix}$.

-   Scalar multiplication. If we have a scalar $\alpha$ and we multiply
    it with a vector $\vec{b}$, this is interpreted as multiplying every
    element in $\vec{b}$ by $\alpha$. Thus scalar multiplication is a
    stretching or compressing (with flipping if $\alpha < 0$) of the
    vector

    <span>Scalar Multiplication</span> Let
    $\vec{b} = \begin{bmatrix}1\\4\end{bmatrix}$ and $\beta=2$.
    $$\begin{aligned}
                \beta\vec{b}=2\begin{bmatrix}1\\4\end{bmatrix}\\
                =\begin{bmatrix}2\cdot 1\\2\cdot 4\end{bmatrix}\\
                =\begin{bmatrix}2\\8\end{bmatrix}
            \end{aligned}$$ Picture.

-   A <span>**linear combination**</span> of vectors is formed by
    scaling and adding the vectors together. This will be an important
    idea when we talk about matrix multiplication.

    <span>Linear Combination of Vectors</span> Let
    $\alpha=2, \beta=3, \text{ and } \gamma=-1$ and $$\begin{aligned}
                \vec{v_1}=\begin{bmatrix}2\\-1\\-4\end{bmatrix},\\
                \vec{v_2}=\begin{bmatrix}0\\1\\0\end{bmatrix},\\
                \vec{v_3}=\begin{bmatrix}1\\1\\3\end{bmatrix}
            \end{aligned}$$ The linear combination
    $\alpha\vec{v_1}+\beta\vec{v_2}+\gamma\vec{v_3}$ is
    $$\begin{aligned}
                2\cdot \begin{bmatrix}2\\-1\\-4\end{bmatrix} +
                3\cdot \begin{bmatrix}0\\1\\0\end{bmatrix} + 
                -1\cdot \begin{bmatrix}1\\1\\3\end{bmatrix} = 
                \begin{bmatrix}3\\0\\-11\end{bmatrix}
            \end{aligned}$$ .

<span>Addition and scalar multiplication of vectors</span> Given vectors
$\vec{u},\vec{v},\text{ and } \vec{w}$ along with scalars $\alpha$ and
$\beta$, then

-   $(u+v)+2=u+(v+w)$

-   $u+0=u$

-   $u+(-u)=0$

-   $u+v=v+u$

-   $\alpha(u+v)=\alpha u + \alpha v$

-   $(\alpha+\beta)u = \alpha u + \beta u$

-   $(\alpha\beta)u=\alpha(\beta u)$

-   $1u = u$

.

Dot Product {#dot-product .unnumbered}
-----------

-   The <span>**dot product**</span> or <span>**inner product**</span>
    is a <span>**very**</span> important idea to understand.

-   The dot product is obtained by multiplying corresponding elements of
    the two vectors and then summing the products.
    $$u\cdot v = \sum_i=0^{N-1}u_i v_i$$

-   The dot product (inner product) measures how parallel two
    vectors are. If the inner product of two vectors is zero, then they
    are <span>**orthogonal**</span>.

-   The angle between two vectors can be measured with the dot product
    $$\cos{\phi} = \frac{\vec{u}\cdot\vec{v}}{{\left|\left|\vec{u}\right|\right|}{\left|\left|\vec{v}\right|\right|}}$$
    where ${\left|\left|\cdot\right|\right|}$ is the
    <span>**norm**</span> or magnitude of the vector.

Vector norms {#vector-norms .unnumbered}
------------

-   ${\left|\left|\vec{u}\right|\right|} = \sqrt{\vec{u}\cdot\vec{u}}$

-   A unit vector is a vector with norm of one. A unit vector can be
    created from any arbitrary vector as follows:
    $$\overset{*}{\vec{u}} = \frac{\vec{u}}{ {\left|\left| \vec{u} \right|\right|} }$$

-   Schwartz inequality:
    $|\vec{u}\cdot\vec{v}|\le{\left|\left|\vec{u}\right|\right|}{\left|\left|\vec{v}\right|\right|}$

-   Triangle inequality:
    ${\left|\left|\vec{u}+\vec{v}\right|\right|}\le{\left|\left|\vec{u}\right|\right|}+{\left|\left|\vec{v}\right|\right|}$


