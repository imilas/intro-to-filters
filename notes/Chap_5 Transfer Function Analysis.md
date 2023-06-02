

## Definition of z-transform
$$
X(z) \triangleq \sum_{n=0}^{\infty}x(n)z^{-n} \quad \text{unilateral, multilateral if starting with $-\infty$} 
$$
$$
\begin{align}
X(z) &= Z_{z}\{x(.)\} \\ \\
&\text{Alternatively} \\\\
X &= Z\{x\}
\end{align}
$$
### Example:
if $x(n) = n+1$ for $0 \le n \le_{2}$ then $X(z) = 1+2z^{-1}+3z^{-2}$

## Shift Theorem
Delay of $\Delta$ in the time domain corresponds to multiplication by $z^{\Delta}$ in the frequency domain.
**Intuition**: when $x(n)=c$ shifted to the right (or delayed) by $\Delta$, all the  $c$ values will be multiplied by an extra $z^{-\Delta}$ . Here, the **causality** assumption is used. A causal signal is one that is 0 prior to time 0, so when the signal is delayed by $\Delta$, the new values inserted are 0. 

proof: https://ccrma.stanford.edu/~jos/filters/Shift_Theorem.html

## Convolution theorem
convolution in the time domain is equal to multiplication in the frequency domain. 
$$
x*y \leftrightarrow X\cdot Y
$$
Using Operator notation
$$
    Z_{z}\{x*y\} = X(z)\cdot Y(z)
    
$$
Proof: https://ccrma.stanford.edu/~jos/filters/Convolution_Theorem.html

## Z-Transform of Convolution
The transfer function of a linear time-invariant discrete-time filter is $H(z)=\frac{Y(z)}{X(z)}$. Where $H(z)$ is the z-transfer of the impulse response $h(n)$ and $Y$,$X$ are the z-transfers of $x(n)$ and $y(n)$. This is because $y(n) = (h*x)(n)$ as we've seen before, and the Z function can be applied to both sides. 

## Z-Transform of General Difference Equation

Applying the Z-transform to both sides of the general difference equation gives us the formula:
$$
H(z) \triangleq \frac{Y(z)}{X(z)} = \frac{b_{0}+b_{1}Z^{-1}+\dots+b_{M}z^{-M}}{1+a_{1}z^{-1}+\dots+a_{n}z^{-N}} \triangleq \frac{B(z)}{A(z)}
$$

Proof: https://ccrma.stanford.edu/~jos/filters/Z_Transform_Difference_Equations.html

### Factored Form:
Some background covered in Chapter 7 Pole zero analysis, see https://ccrma.stanford.edu/~jos/filters/Pole_Zero_Analysis_I.html


## Series and parallel Transfer Functions
1. Transfer function of filters in series multiple: [proof](https://ccrma.stanford.edu/~jos/filters/Series_Case.html)
2. Transfer function of filters in parallel sum [proof](https://ccrma.stanford.edu/~jos/filters/Parallel_Case.html)
Remember that:
$$
y(n) = (h*x)(n)
$$
and 
$$
Y(z) = H(z)X(z)
$$
So if a signal $x$ is being processed in a series with $H_1$ and $H_{2}$ then $X$ will be multiplied by $H_{z} =H_{1}\cdot H_{2}$. If $X$ is being processed in parallel then a copy of $X$ is multiplied individually by each transfer function and summed. 

Note that the above suggests that the ordering of filters is commutative since multiplication of the filters is commutative.  

## Partial Fraction Expansion
If $M<N$ (strictly proper transfer function), we can describe the transfer function as: 
$$
H(z) = \frac{B(z)}{A(z)} = \sum_{i=0}^{N} \frac{r_{i}}{1-p_{i}z^{-1}}
$$
Where $B(z)$ and $A(z)$ are the coefficients described in [earlier section](#Z-Transform of General Difference Equation). and $r_{i}$ is 
$$
(1-p_{i}) H(z) |_{z=p_{i}}
$$
$r_{i}$, or the residue, is the coefficient of the one-pole term $\frac{1}{1-pz^{-1}}$ as the $z\to p_{i}$ 

 > every strictly proper transfer function (with distinct poles) can be implemented using a parallel bank of two-pole, one-zero filter sections.

See example at: https://ccrma.stanford.edu/~jos/filters/Example.html
see complex example: https://ccrma.stanford.edu/~jos/filters/Complex_Example.html 

## Inverse Transform
We have
$$
H(z)= \sum_{i=0}^{N} \frac{r_{i}}{1-p_{i}z^{-1}}
$$
So each $H_{i}(z)=\frac{r_{i}}{1-p_{i}z^{-1}}$ 
Which is the geometric series 
$$
\sum_{n=0}^{\infty} r_{i}p_{i}^{n}z^{-n}
$$
Which is the z-transform of $h_{i}(n)=r_{i}p_{i}^{n}$. 

So the inverse z-transform of $H(z)$ is $h(n)$:
$$
h(n) = \sum_{i=1}^{N}h_{i}(n) = \sum_{i=1}^{N}r_{i}p_{i}^{n}, \quad n=0,1,2,\dots
$$
> Thus, the [impulse response](https://ccrma.stanford.edu/~jos/filters/Impulse_Response_Representation.html) of every strictly proper [LTI filter](https://ccrma.stanford.edu/~jos/filters/Linear_Time_Invariant_Digital_Filters.html) (with distinct [poles](https://ccrma.stanford.edu/~jos/filters/Pole_Zero_Analysis_I.html)) can be interpreted as a _[linear combination](https://mathworld.wolfram.com/LinearCombination.html) of sampled complex [exponentials](https://ccrma.stanford.edu/~jos/mdft/Exponentials.html)_. Recall that a uniformly sampled [exponential](https://ccrma.stanford.edu/~jos/mdft/Exponentials.html) is the same thing as a _[geometric sequence](https://en.wikipedia.org/wiki/Geometric_progression)_. Thus $h$ is a linear combination of $N$ geometric sequences. 

## FIR Part of PFE
If M>N, then we'll have an FIR part to the PFE. 
$$
H(z) = \frac{B(z)}{A(z)} = F(z) + \sum_{i=0}^N \frac{r_{i}}{(1-p_{i}z^{-1})}
$$
Where $F(z) = f_{0} + f_{1}z^{-1} + \dots + f_{2}z^{-k}$ and $k=M-N$

There are two main approaches for this scenario, see : https://ccrma.stanford.edu/~jos/filters/FIR_Part_PFE.html

## Repeated Poles
Assume there are two identical poles in parallel and in a series:
    In a series, they multiply, so we will have a two pole filter with a repeated pole. 
    In parallel, we will have a one pole filter with a new residue value.

## Dealing with Repeated Poles Analytically:
Assuming there is a pole $p_{i}$ repeated $m_{i}$ times. A pole with multiplicity $m_{i}$ has $m_{i}$ coefficients. 
$r_{ij}$ is the $j$th coefficient associated with pole $p_{i}$ then each $r_{ij}$ is defined by: (note that $j$ starts from 0):
$$
r_{ik} = \frac{1}{(k-1)!(-p_{i})^{k-1}} \cdot \frac{d^{k-1}}{d(z^{-1})^{k-1}}(1-p_{i}z^{-1})^{mi}H(z)|_{z=p_{i}} 
$$


See example: https://ccrma.stanford.edu/~jos/filters/Dealing_Repeated_Poles_Analytically.html

## Impulse Response of Repeated Poles
In the time domain, repeated poles give rise to _polynomial [amplitude envelopes](https://en.wikipedia.org/wiki/Envelope_(waves))_ on the decaying [exponentials](https://ccrma.stanford.edu/~jos/mdft/Exponentials.html) corresponding to the (stable) poles. For example, in the case of a single pole repeated twice, we have:

$$
\frac{1}{(1-pz^{-1})^{2}}=\mathcal{Z}\{(n+1)p^{n}\} \leftrightarrow  (n+1)p^{n}
$$
proof: https://ccrma.stanford.edu/~jos/filters/Impulse_Response_Repeated_Poles.html

Here, $p^{n}$ is the decaying exponential and $n+1$ is the first order polynomial amplitude envelope. 
For a pole repeated 3 times, we would have a second order (quadratic) amplitude envelope multiplied by an exponential decay ($p<1$). Exponential decay will overtake polynomial growth eventually so the impulse response always decays to 0. 

> Repeated poles give rise to polynomial envelopes on the exponential decay due to the poles. Two different poles yield a convolution (or sum) of two different exponential decays with no polynomial envelope.

Looking at the convolution of the impulse responses of two poles, $h_{1}=p_{1}^{n}$ and $h_{2}=p_{2}^{n}$, we get:
$$
h(n) = (h_{1}*h_{2})(n) = \sum_{m=0}^{n}p_{1}^{m}\cdot p_{2}^{n-m}=p_{2}^{n}\sum_{m=0}^{n}\left( \frac{p_{1}^{m}}{p_{2}^{m}} \right) 
$$
if $p_{1}=p_{2}=p$  then this yields $h(n) = p^{n} \cdot(n+1)$ 
Else, we [continue the simplification](https://ccrma.stanford.edu/~jos/filters/So_What_s_Up_Repeated.html) to get: 
$$
h(n) = \frac{p_{1}^{n+1}-p_{2}^{n+1}}{(p_{1}-p_{2})}
$$

## Important examples:
see bottom of https://ccrma.stanford.edu/~jos/filters/Example_General_Biquad_PFE.html
Especially state space filters: https://ccrma.stanford.edu/~jos/filters/State_Space_Filters.html

Summary: 
https://ccrma.stanford.edu/~jos/filters/Summary_Partial_Fraction_Expansion.html
# Further Reading
https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra
Circuits: 
    - https://learn.sparkfun.com/tutorials/what-is-a-circuit/all
Envelopes: https://en.wikipedia.org/wiki/Envelope_(waves)
## Questions
Prove the PFE formula mathematically. 