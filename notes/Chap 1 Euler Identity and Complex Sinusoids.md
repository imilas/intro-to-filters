
# Taylor Series
$$
f(x) = \sum_{n=0}^{\infty} { \frac{f^{(n)}(x_0)}{n!} . (x-x_0)^n  }
$$
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
Think of this as the rate for constant growth. See further reading. 


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
### complex sinusoid: 
$$
e^{j(\omega*n*T+\phi)}
$$



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
These are M equally spaced values on the unit circle. Different k values correspond to the complex sinusoids that are used in DFT for analysis of different frequencies

# De Moivre Theorem

$$
 (\cos(x)+i\sin(x))^n = \cos(nx)+i\sin(nx) 
$$
Easy to prove using euler's identity.
This establishes that integer powers (only integer powers?) of $\cos(x)+i\sin(x)$ line up on the unit circle. 


# complex sinusoids
This is $Ae^{j(\omega t+\phi)}$ for continuous and $Ae^{j(\omega nT+\phi)}$ for discrete cases.

$$
\begin{align} 
\cos(\theta) = \frac{e^{j\theta}+e^{-j\theta}}{2} \\
\sin(\theta) = \frac{e^{j\theta}-e^{-j\theta}}{2} \\
\end{align}
$$
The above equations show that $\cos$ and $\sin$ are less fundimental than $e^{j\theta}$. Note that using real linear operations on complex sinusoids will treat the real and imaginary parts independently. 
Another takeaway is that a real sinusoid is the equal combination of a positive and negative frequency components. (this comes up when taking fourier transforms?)

## Phasor
$\mathcal{A} \triangleq Ae^{j\phi}$ is the complex amplitude/phase of the complex sinusoids. It will off set the phase by $\phi$ and change amplitude from 1 to A. This is also known as the phasor of the sinusoid.

# General LTI filter effects
in general, an LTI filter can only chnage the amplitudes and phases of the frequencies in a signal. Any LTI filter is completely characterized by it's relative gain $\frac{A_{1}}{A_{2}}$ and phase $\phi_{1}-\phi_{2}$ change at each frequency 
![[Pasted image 20230508113643.png]]


# further reading
https://betterexplained.com/articles/intuitive-understanding-of-eulers-formula/
https://www.dsprelated.com/freebooks/mdft/Sinusoids_Exponentials.html
