# Signal Definition
$$
\begin{align}
x(n) &= z \text{ where } z \in Z  \\
&or \\
x(n) &= c \text{ where }c \in \mathcal{C}
\end{align}
$$
a signal may be finite or infinite length
# Filter Defitinion
a real or complex mapping of $x(n)$ to $y(n)$ for every n. 
$$
\begin{align}
&\text{where $\mathcal{S}$ is the signal space}\\
&y(n) = \mathcal{T}\{x(.)\} \\
&X \in \mathcal{S} \to Y \in \mathcal{S} \\
\end{align}
$$
If $\mathcal{S}$ only consists of N length signals then every linear filter $\mathcal{T}$ can be represented as an NxN matrix

# LTI Filters
LTI filters are the only filters which preserve signal frequencies (prove)
- Linearity: that each output at time n is a linear combination of signals, the coefficients of which do not depend on the inputs or outputs (x or y). Scaling and superposition properties are required. See more at [Linearity](#linearity)
- Time-invariance means that the coefficients applied to the input(s) do not vary with time.

Example: $y(n) = c_{1}x(n) + c_{2}x(n+1)$
- The coefficients can be complex or real, and the filter will remain LTI. 
- This is an example of a non-causal filter, since it uses $x(n+1)$, therefore needs knowledge of the future. 
- Use of past outputs $y(n)$ is called *feedback* or *recursive* filters. 
Example of a multi-input multi-output (MIMO) filter
$$
\begin{bmatrix}
y_{1}(n) \\
y_{2}(n)
\end{bmatrix}=
\begin{bmatrix}
a & b \\
c & d 
\end{bmatrix}
\begin{bmatrix}
 x_{1}(n) \\
x_{2}(n)
\end{bmatrix}+
\begin{bmatrix}
e & f \\
g & h
\end{bmatrix}
\begin{bmatrix}
x_{1}(n-1) \\
x_{2}(n-1)
\end{bmatrix}
$$
### Non-linear filters
Simplest example, which is also memoryless $$y(n) = x^{2}(n)$$
Another example is a median smoother of order N which uses the median of N samples centered around time n to determine the output at time n. 

## Time variant filters
Example: 
$$
y(n) = x(n) + \cos(2\pi n)x(n-1)
$$
is time-variant because the coefficient changes depending on n. It is linear however because no coefficients depend on x or y.

# Linearity
2 properties have to hold for linearity
	- Scaling: The amplitude of the output is proportional to the amplitude of the input (the _scaling property_).
	- Superposition: When two [signals](http://ccrma.stanford.edu/~jos/filters/Definition_Signal.html) are added together and fed to the [filter](https://ccrma.stanford.edu/~jos/filters/What_Filter.html), the filter output is the same as if one had put each signal through the filter separately and then added the outputs (the _superposition property_).

## Mathmatical Definition
Let's say $\mathcal{L}$ is a linear, but not necessarily time-invariant filter. The output is dependent on 1 or more of x's variables, which is why we use $x(.)$. 
$$
y(n) =\mathcal{L_{n}(x(.))}
$$
$\mathcal{L_{n}}$ is said to be linear if:

$$
\begin{align}

\text{Scaling} &: \mathcal{L_{n}\{gx(.)\}} = g\mathcal{L_{n}\{x(.)\}} \quad \forall g \in C, \forall x \in \mathcal{S} \\
\text{Superposition}&: \mathcal{L_{n}}\{x_{1}(.)+x_{2}(.)\} = \mathcal{L_{n}\{x_{1}(.)\}+\mathcal{L_{n}}\{x_{2}(.)\}} \quad \forall x_{1},x_{2} \in \mathcal{S}\end{align}
$$
Where $\mathcal{S}$ denotes signal space, or complex values sequences in general. 

### Real Filtering of Complex Signals
$$
\begin{align} \\
w &=  x+jy\\

\mathcal{L_{n}\{w\}} &\triangleq \mathcal{L_{n}}\{x\} + j\mathcal{L_{n}}\{y\} 

\end{align}
$$
This means that applying a filter to a complex signal will treat the real and complex parts seperatly

## Time invariance:
If the input is shifted by N samples,  the output is shifted by N samples. 
$$
\mathcal{L_{n}}\{SHIFT_{N}(x)\} = \mathcal{L_{n}}\{\text{SHIFT}_{N,n} (y)\} = \mathcal{L_{n-N}\{x\})} = y(n-N)
$$
$$
\text{where : }\mathcal{L_{n}}\{SHIFT_{N}(x)\} \triangleq x( . - N)
$$
## Sliding linear combinations
$$
y(n) = b_{1}x(n) +b_{2}x(n-1) 
$$
Any filter of the above form is linear and time invariant, and is a special case of sliding linear combination/weighted sum. Time invariance depends on b being a constant. 
By induction, it can also be proven than adding a feedback term to these filters remains linear and time-invariant (see [problems](###Problems and proofs) )

## Problems and proofs
See https://ccrma.stanford.edu/~jos/filters/Showing_Linearity_Time_Invariance.html
Question: is $y(n) = c$ linear or time-invariant?

## further reading
volterra series, can represent every non-linear system: https://ccrma.stanford.edu/~jos/filters/Analysis_Nonlinear_Filters.html
dynamic convolution, used for mapping memory-less non-linear functions followed by and LTI: https://www.uaudio.com/webzine/2004/july/text/content2.html
