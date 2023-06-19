The frequency response yields phase and gain shift as a function of frequency. 
We have seen that
$$
y(z) = H(z)X(z)
$$
If we set $z = e^{j\omega T}$ where $\omega$ is a real radian frequency and $T$ is $\frac{1}{f_{s}}$ where $f_{s}$ is the sampling rate, we get the *DTFT* or discrete time fourier transform. 

The bilateral *DTFT* where T is normalized to 1 is 
$$
X(e^{j\omega T}) = \sum_{n=-\infty}^{\infty}x(n)e^{-j\omega Tn}
$$
Where $x$ is causal, we get the unilateral DTFT
$$
\text{DTFT}_{w}(x) = \sum_{n=0}^{\infty} x(n)e^{-jwn}
$$
So the spectrum of the output is equal to the spectrum of the input times the spectrum of the impulse response. So
> The frequency response of an LTI is equal to the transfer function evaluated on the unit circle in the $z$ plane i.e $H(e^{jwT})$
> This means that the frequency reponse is the DTFT of the fourier transform

$$
H(e^{jwT}) = DTFT_{\omega T}(h)
$$
We typically restrict $\omega$ to $[-\pi,\pi]$

The frequency response can also be represented in polar form as:
$$
H(e^{j\omega T}= G(\omega)e^{j\phi(\omega)})
$$
Where $G(\omega)\triangleq|H(e^{-j\omega T})$ is the magnitude and $\phi(\omega) \triangleq \angle H(e^{-j\omega T})$

This implies:
$$
|Y(e^{jwT})| = g(\omega)|X(e^{jwT})|
$$
$$
\angle(Y(e^{jwT}) = \phi(\omega)+\angle X(e^{j\omega T})
$$
$$Y(e^{j\omega T})=|Y(e^{j\omega T})|\cdot e^{\angle Y(e^{j\omega T})}$$

if $a=re\{H(e^{jwt})\}$ and $b=im\{H(e^{jwt})\}$ then
$$
\begin{gather}
G(\omega)=\sqrt{ a^{2} + b^{2} }\\
\phi(\omega) = \tan ^{-1}\left( \frac{b}{a} \right)\\
a = G(\omega)\cos(\phi(\omega))\\
b = G(\omega)\sin(\phi(\omega))
\end{gather}
$$
## Seperating numerator and denominator
$$
H(z) = \frac{B(z)}{A(z)}
$$
Gives:
$$
g(\omega) = |\frac{B(e^{j\omega T})}{A(e^{j\omega T})}| 
$$
$$
\phi(\omega) = \angle B(e^{j\omega T})-\angle A(e^{jwt})
$$
## DFT Definition
$$
DFT_{\omega_{k}}T(x) = \sum_{n=0}^{N_{s}-1}x(n)e^{-j\omega_{k}nT}
$$
Where $\omega\triangleq \frac{2\pi f_{s}k}{N_{s}}$ and $f_{s}=\frac{1}{T}$ 

This might? reduce to:
$$
DFT_{wk} =\sum_{n=0}^{N_{s}-1} x(n)e^{-j2\pi k/N_{s}} \quad k=0,1,2,\dots N_{s}-1
$$
The inverse is defined as:
$$
h(n) = IDFT_{n}(H) \triangleq \frac{1}{N_{s}}\sum_{k=0}^{N_{s}-1}H(k)e^{j2\pi k/N_{s}}
$$
The choice of $N_{s}$ is typically $\frac{N_{s}>7}{(1-R_{max})}$, see https://ccrma.stanford.edu/~jos/filters/Frequency_Response_Matlab.html

## Phase Delay
The phase delay $\phi(\omega)$ gives the radian phase shift added to the phase of each sinusoidal component of the input signal. $P(\omega)$ is defined as 
$$
P(\omega) \triangleq - \frac{\phi(\omega)}{\omega}
$$
which gives the time delay in seconds for each sinusoidal component. 
If an input $x(n) = \cos(\omega nT)$ is given to $H(e^{j\phi T})=G(\omega)e^{-j\phi(\omega)}$
The output is 
$$
Y(n) = G(\omega)\cos(\omega(nT-p(\omega)))
$$
## Group Delay
$$
D(\omega) = -\frac{d(\phi(\omega))}{d(\omega)}
$$
This would be identical to phase delay when if the phase response is linear. 
The "group" in the name refers to the fact that it specifies the delay experienced by a narrow band of sinusoidal components around the frequency $\omega$ where the phase response is linear. 

Derivation (wtf?): https://ccrma.stanford.edu/~jos/filters/Derivation_Group_Delay_Modulation.html