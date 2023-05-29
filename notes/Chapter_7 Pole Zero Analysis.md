In previous chapters we saw that the transfer function for the recursive LTI filter is:
$$
H(z) = \frac{g(1+\beta_{1}z^{-1}+\beta_{2}z^{-2}+\dots+\beta_{M}z^{-M})}{1+\alpha_{1}z^{-1}+\alpha_{2}z^{-2}+\dots+\alpha_{N}z^{-N}}
$$
We know that the polynomials in the numerator and denominator can be factored, giving the form:
$$
H(z) = \frac{g(1-q_{1}z^{-1})(1-q_{2}z^{-1})\dots(1-q_{M}z^{-1})}{(1-p_{1}z^{-1})(1-p_{2}z^{-1})\dots(1-p_{N}z^{-1})}
$$
Assuming none of the terms in the numerator and denominator cancel out, poles are points where $z$, a complex number, is equal to any of the $p_{i}$ values. Zeroes are when $z$ is equal to the $q_{i}$ values. We can think of $z$ values lying on a 2D plane, and the $H$ magnitude, which is a real number being the 3rd dimension that lies above the z-plane. $q_{i}$ and $p_{i}$ values would be points where the $H$ magnitude is either infinitely small (zero) or large (resembling a pole). 

Also note that the filter order is either $M$ or $N$, or the number of poles or zeros, whichever is greater. **So the order of an LTI filter is the order of its transfer function.**

## Graphical Computation of Amplitude Response
If we take the factored form of the transfer function and set $z$ to $e^{jwt}$, we get the frequency response in factored form:
$$
H(z) = \frac{g(1-q_{1}e^{-jwt})(1-q_{2}e^{-jwt})\dots(1-q_{m}e^{-jwt})}{(1-p_{1}e^{-jwt})(1-p_{2}e^{-jwt})\dots(1-p_{N}e^{-jwt})}
$$
The amplitude response $G(w) = |H(e^{jwt})|$ ends up being:
$$
G(w) = |g| \frac{|e^{jwt}-q_{1}| |e^{jwt}-q_{2}|\dots|e^{jwt}-q_{M}|}{|e^{jwt}-p_{1}|\dots|e^{jwt}-p_{M}|}
$$
proof: https://ccrma.stanford.edu/~jos/filters/Graphical_Amplitude_Response.html

Consider that the magnitude of vector $u-v$ is a point drawn from the tip of $v$ to $u$. 
This leads to the following conclusion:
    > The frequency response magnitude (amplitude response) at frequency $w$ is given by the product of lengths of vectors drawn from the zeros to the point $e^{jwt}$ divided by the product of vectors drawn from the poles to the point $e^{jwt}$. 
## Computation of Phase Response 

$$
\begin{gather}
\Theta(\omega) \triangleq \angle g + (N-M)\omega T + \angle(e^{jwT}-q_{1})+\angle(e^{jwT}-q_{2})+\dots+\angle(e^{jwT}-q_{M})\\-\angle(e^{jwT}-p_{1})-\angle(e^{jwT}-P_{2})-\dots \angle(e^{jwT}-p_{N}) 

\end{gather}
$$
Proof:https://ccrma.stanford.edu/~jos/filters/Graphical_Phase_Response_Calculation.html

The additional term $(N-M)\omega T$ arises when we consider a $z^{N-M}$ term in the transfer function, with poles/zeros at $z=0$.
$$
H(z) = g z^{N-M} \frac{(z-q_{1})(z-q_{2})\dots(z-q_{M})}{(z-p_{1})(z-p_{2})\dots(z-p_{N})}
$$
### Question: 
Can you write a simple function to calculate the phase response graph here?
https://ccrma.stanford.edu/~jos/filters/Graphical_Phase_Response_Calculation.html

## Further reading
analytic function: https://mathworld.wolfram.com/AnalyticFunction.html
Conformal mapping: https://mathworld.wolfram.com/ConformalMapping.html
