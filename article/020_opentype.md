# [Analyzing Variation Models](https://typeof.net/2019/analyzing-variation-model/)

I am surprised that nobody actually did a mathematical analysis of the variation model in OpenType. They are simply reusing the concepts of the old MM system, and complicating the things they need.

## Standard variations

For almost all places in a current variable font, anything that varies (coordinates, lengths, parameters, etc.) could be expressed in the following model:

$\hat{x}(v) = \bar{x} + \sum_{m \in \mathfrak{M}_x} D_x[m] \, W(m,v)$ (1)

$W(m,v) = \prod_{a \in \mathfrak{A}} \Lambda(m[a], v[a])$ (2)

The notation $\hat{x}$ denotes a variable quantity (VQ), which responds to an instance tuple $v$. $\bar{x}$ is the default value of $\hat{x}$. $\mathfrak{M}_x$ represents the region set of $\hat{x}$, and $D_x[m]$ is the delta associated with this master $m$. Binary function $W(m,v)$ computes the weight of master $m$ under instance $v$, which is defined as a product of axis weights.

We can easily conclude that VQs form a linear space, since scalar product and sum can be defined in such manner:

$(s \cdot \hat{x})(v) = s \bar{x} + \sum (sD_x[m]) W(m,v)$ (3)

$(\hat{x}+\hat{y})(v) = (\bar{x}+\bar{y}) + \sum (D_x[m]+D_y[m])W(m,v)$ (4)

One thing we could not define yet is the product of two VQs, we’d like to discuss them later.

You’ve noticed that the entire variation model is a sum, instead of blending values across masters. However, conversion from blending into VQ could be easily achieved by solving a linear system.

## Nested variations

One interesting special case happens in CFF2: in theory, the `blend` operators in CFF2 could be nested, so equation (1) would be modified into this form:

$\hat{x}(v) = \bar{x} + \sum_{m \in \mathbb{M}_x} \hat{D}_x[m](v) \, W(m,v)$ (5)

The only difference is that the factor $\hat{D}_x[m](v)$ is now a VQ instead of a number. However the property that VQs form a linear space still holds, since we can recursively scale or sum VQs in (5).

## Products of variations

One thing we’d like to extend current standard is allowing products $(\hat{x} \cdot \hat{y})$ be representable in the variation system, and that is surprisingly simple by allowing axes to repeat in masters (variation regions). The product

$(\hat{x} \cdot \hat{y})(v) = \bar{x} \cdot \bar{y}$ (6)

$+(\bar{x} \cdot \hat{y})(v)$ (7)

$+(\bar{y} \cdot \hat{x})(v)$ (8)

$+ \sum_{m_x\in\mathfrak{M}_x} \sum_{m_y\in\mathfrak{M}_y} (D_x[m_x] \cdot D_y[m_y])W(m_x,v)W(m_y,v)$ (9)

The term (6), (7), (8) are simply scales of VQs, but term (9) contains product of weight functions that is not representable in the current standard. However releasing this restriction is surprisingly simple: we can allow masters to contain an axis list, which may have duplicate axes, and associate a “tent” (start-peak-end triplet) to each axis item. In the current standard, the axis list is a fixed list shared across the entire font.

In other terms, the form of (2) would be modified into this form:

$W(m,v) = \prod_{(a,\tau)\in\mathfrak{A}[m]} \Lambda(\tau,v[a])$ (10)

Notation $\mathfrak{A}[m]$ denotes the “axis-tent” list that forms this master, and we do the same product just like the old definition. Then the product of two weighting functions could be defined as:

$W(m_x,v)W(m_y,v) = \prod_{(a,\tau)\in\mathfrak{A}[m_x]\mathfrak{A}[m_y]} \Lambda(\tau,v[a])$ (11)

where notation $\mathfrak{A}[m_x]\mathfrak{A}[m_y]$ denotes we simply concatenate the axis-tent lists together.

## Mutatormath, etc.

Mutatormath and libraries similar to that defines how we convert a set of peak tuples into a master set, where each master requires each axis’ record having a start and an end, as well as the peak already given. Once the master set is decided, the interpolation part could be easily done by solving linear systems.

# [On High-order Interpolation and Non-linear Interpolation](https://typeof.net/2021/on-hoi-and-nli/)

Defining a mechanism to represent polynomials in OtVar’s mechanism is possible, if one axis value could be assigned to multiple axes. From the equation (2) in the previous article, if in v we have $v_0 = v_1 = t$, then we could define a region m that satisfies $W(m,v)=t^2$ by making the axis region $m_0$ and $m_1$ as axis regions that peaked at $1$. Terms with higher degree could also be constructed in the similar manner.

Actually, with duplicate axis, we could define a ring for variable quantities, since the multiplication:

$(\hat{x} \cdot \hat{y})(v) = \bar{x} \cdot \bar{y}$ (1)

$+ \bar{x} \cdot \sum_{m\in\mathfrak{M}_y} D_y[m]W(m,v)$ (2)

$+ \bar{y} \cdot \sum_{m\in\mathfrak{M}_x} D_x[m]W(m,v)$ (3)

$+ \sum_{m_x\in\mathfrak{M}_x} \sum_{m_y\in\mathfrak{M}_y} D_x[m_x]D_y[m_y]W(m_x,v)W(m_y,v)$ (4)

Part (1), (2), (3) are already representable in OtVar, and in the part (4), we could use duplicate axes to ensure that for any region pair $m_x$ and $m_y$, their axis index set does not overlap, which made the product $W(m_x,v)W(m_y,v)$ representable in the OtVar form.

If OtVar could further extended to support non-linear variation, the simplest change is to add a degree parameter to each region, which changes the region-weighting function into:

$W\prime(m,v) = \prod_{a\in\mathfrak{A}} \Lambda(m[a],v[a])^{d[m[a]]}$ (5)

where $d[m[a]]$ denotes the degree parameter of axis region $m[a]$.

# [Integrals of variable values](https://typeof.net/2022/integrations-of-variable-values/)

This is an open problem about “variable values” in variable fonts.

Consider the variable value model we discussed in previous posts:

$\hat{x}(v) = \bar{x} + \sum_{m\in\mathfrak{M}_x} D_x[m] W(m,v)$ (1)

$W(m,v) = \prod_{a\in\mathfrak{A}}\Lambda(m[a],v[a])$ (2)

We could consider the integral of a variable value over the design space:

$\int_\mathfrak{B} \hat{x}(v)dv$ (3a)

... or defining inner products of variable values:

$\hat{x} \cdot \hat{y} = \int_\mathfrak{B} \hat{x}(v)\hat{y}(v)dv$ (3b)

Computing such integrals’ exact value might be non-trivial, though, acquiring an numeric result is not hard.

Being able to define inner products is helpful for certain font processing processes, for example, cubic-to-quadratic conversion. In this process, we are converting an arc $A(t)$ to its approximation $\tilde{A}(t)$. We could measure the overall conversion error as:

$\int_t |A(t)−\tilde{A}(t)|$ (4)

Where normals $|x|$ could be defined as $\sqrt{x \cdot x}$.
