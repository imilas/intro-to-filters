![[Pasted image 20230502122236.png]]
 
# common angles
![[Pasted image 20230503133621.png]]

# useful identities
![[Pasted image 20230504141725.png]]
![[Pasted image 20230525113039.png]]
# Latex snippets:


https://github.com/artisticat1/obsidian-latex-suite/blob/main/src/default_snippets.ts
https://github.com/artisticat1/obsidian-latex-suite
https://castel.dev/post/lecture-notes-1/

# Taylor Series
$$
f(x) = \sum_{n=0}^{\infty} { \frac{f^{(n)}(x_0)}{n!} . (x-x_0)^n  }
$$
### Power Series
Arise as taylor series of infinitely differentiable functions. Have the form

$$
\sum_{n=0}^{\infty}a_{n}(x-c)^{n}
$$
Where c is the **center** of the series. If center of the series is 0, then we get the maclauren series. 

# geometric series
$$ 
\begin{gather}
\sum_{k=0}^{\infty} ar^k {\rightarrow} \text{generator term} \\
\frac{a}{1-r} \text{ for |r|} \textless1
\end{gather}
$$

# Euler's number
$$
e = \lim_{\delta->0}({1+\delta})^{1/\delta}
$$
Think of this as the rate for constant growth. 
$$
\begin{equation}
	
\end{equation}
$$

# Eulers Identity
$$
e^{j\theta} = cos(\theta) + jsin(\theta)
$$
### Continuous
$$
e^{j(\omega t + \phi)} = \cos(\omega t + \phi) + j\sin(\omega t + \phi)
$$
## discrete
$$
e^{j(\omega n T + \phi)} = \cos(\omega n T + \phi) + j\sin(\omega n T + \phi)
$$
complex sinusoid: $e^{j(\omega*n*T+\phi)}$ 


## proof:
$$
e^{x} = \sum_{n=0}^{\infty} {\frac{x^n}{n!}} = 1 + x + \frac{x^2}{2} + ... \text{ using taylor series}
$$

$$
\begin{equation}
\begin{aligned}
e^{j\theta} &= 1 + j\theta + \frac{(j\theta)^2}{2} +\frac{(j\theta)^3}{3!} +...\\
&= 1 + j\theta - \frac{\theta^2}{2} -\frac{j\theta^3}{3!} + ...\\

\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
re\{e^{j\theta}\} &= 1 -\frac{\theta^{2}}{2} + \frac{\theta^4}{4!} \\

im\{e^{j\theta}\} &= j\theta-\frac{j\theta^{3}}{3!} + \frac{j\theta^5}{5!}
\end{aligned}
\end{equation}

$$
![[Pasted image 20230502162443.png]]

# Mth Roots

Any real or complex number $z$ can be represented with $re^{j\theta}$, which can represent any point in a 2D space. Here, theta would be $\tan^{-1}\left( \frac{a}{b} \right)$ where a and b are the real and imaginary coordinates.

$$
\begin{align} \\

1 &= e^{2j\pi k} = \cos{2\pi\theta} + j*0\\ 
z &= re^{j\theta}e^{2j\pi k} \\
z^{1/M} &= r^\left( \frac{1}{M} \right)e^{j\frac{\theta}{M}} e^\left( \frac{2\pi jk}{M} \right) \\
\end{align}
$$
	The formula above  has M unique answers for every positive integer k<M. $r^\left( \frac{1}{M} \right)$ will grow into $r$ and $(e^\frac{j\theta+2\pi k}{M})^M$ will rotate to the correct angle for every integer value of k.
# Roots of Unity
$$
1^{k/M} = e^{2\pi j\frac{k}{M}}
$$
These are M equally spaced values on the unit circle. Different k values correspond the the complex sinusoids that are used in DFT for analysis of different frequencies


# De Moivre Theorem

$$
 (\cos(x)+i\sin(x))^n = \cos(nx)+i\sin(nx) 
$$
Easy to prove using euler's identity.
This establishes that integer powers (and only integer powers?) of $\cos(x)+i\sin(x)$ line up on the unit circle 


# Circuits:
Common terms:
    - **Voltage** is the difference in charge between two points.
    - **Current** is the rate at which charge is flowing.
    - **Resistance** is a material's tendency to resist the flow of charge (current).
    - **Amps** Amount of current flowing over a period 

In water terms:
    -   Water = Charge (measured in Coulombs)
    -   Pressure = Voltage (measured in Volts)
    -   Flow = Current (measured in Amperes, or "Amps" for short)
    -   Hose Width = Resistance

$$
    V = I \cdot R
$$
Where:
    -   V = Voltage in volts
    -   I = Current in amps
    -   R = Resistance in ohms

### Series vs Parallel Circuits
Series:
    - V changes as it flows through resistance components
    - I stays the same
    - V = $v_{1} +v_{2}+\dots$
Parallel:
    - V stays the same
    - I changes through the components
    - $v = v_{1} = v_{2}= v_{3}$

## External Notebooks
https://karlhiner.com/jupyter_notebooks/intro_to_digital_filters/
https://github.com/khiner/notebooks/tree/master/introduction_to_digital_filters
# Other Links
circuits: https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law