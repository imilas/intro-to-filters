## Difference equation
$$
y(n) = \sum_{i=0}^N b_{i}x(n-i) - \sum_{j=1}^Ma_{j}y(n-M)
$$
If $a_{j}\gt_{0}$ for some j, then the filter is called recursive, or an infinite impulse **IIR** filter
Else, there is no feedback and the filter is a finite impulse response **FIR** filter. This equation only represents causal filters. 

## Impulse response
$$
h(n) \triangleq \mathcal{L_{n}}\{\delta(.)\}
$$
Where $\delta = [1,0,0,0,\dots]$ 
Any LTI filter can be applied by convolving the signal with the filter's impulse response $h(n)$.
The impulse response has to decay to zero as $n\to \infty$, otherwise it is unstable 

### Convolution
$$
f*g(t) = \int_{-\infty}^{\infty} f(\tau)g(t-\tau) \, d\tau 
$$
Think of this as the entirety of $f$ being weighted by the reflection of $g$. This reflection is shifted to the right (towards infinity) one time-step at a time.


## Representing Filter via Impulse 

Each sample in signal $x(n)$ can be thought of as a scaled and shifted impulse response. The entirety of the signal can be represented as the sum of scaled and shifted impulse responses. Remember that LTI filters have scalability, superposition, and time-invariance properties. Therefore,  we can scale and shift the impulse response of the filter according to the value and index of each $x(n)$, and superimpose the results to get $y(n)$, which is equivalent to applying the filter to the signal. 

### Mathematical definition 
A signal can be represented via its convolution with an impulse response.
$$
x(.) = \sum_{i=0}^n x(i)\delta(i-n) \triangleq (x*\delta)(.)
$$
This might seem redundant, but it shows that we can express $x(n)$ as a linear scaled sum of impulses. Furthermore, using the definition  $h(n) \triangleq \mathcal{L_{n}}\{\delta(.)\}$, we can derive:
$$
\begin{align}
y(n) = \mathcal{L_{n}}\{x(.)\} &= \mathcal{L_{n}}\{(x*\delta)(.)\} \\
& = \mathcal{L_{n}}\left\{ \sum_{i=-\infty}^\infty x(i)\delta(.-i) \right\} \\
& = \sum_{i=-\infty}^\infty x(i) \mathcal{L_{n}}\{\delta(.-i)\}  \\
& \triangleq \sum_{i=-\infty}^\infty x(i) h(n,i)
\end{align}

$$
Here, think of $h(n,i)$ as the filter response at time n to an impulse that occurred at time i. So at each time-step n, the output value is equal to the scaled sum of shifted impulses. 
Reminder that x(i) is a scalar, h(n,i) is a vector. 


If in addition to being linear, the filter is also time-invariant, then we can write $h(n,i) =h(n-i)$, which gives us:
$$
y(n) = \sum_{i=-\infty}^\infty x(i) h(n-i) \triangleq (x*h)(n), \quad  n \in Z
$$
Assuming the filter is linear, time-invariant *and* causal:
$$
y(n) = \sum_{i=0}^n x(i) h(n-i) \triangleq (x*h)(n), \quad  n \in [0,1,2,\dots]
$$
Since convolution is commutative, we also have:
$$
y(n) = \sum_{i=0}^n h(i) x(n-i) =  (x*h)(n), \quad  n \in [0,1,2,\dots]
$$
or 
$$
y(n) = h(0)x(n) + h(1)x(n-1) + h(2)x(n-2) \dots h(n)x(0)
$$
It is also evident that the filter operates by summing _weighted echoes_ of the input signal together. At time $n$, the weight of the echo from $i$ samples ago $[x(n-i)]$ is $h(i)$

## Causal FIR filter definition
FIR filters can be represented by tapped delay line graphs. A [tapped delay line](https://ccrma.stanford.edu/~jos/pasp/Tapped_Delay_Line_TDL.html)  can only implement _finite-duration_ responses in the sense that the non-zero portion of the impulse response must be finite. This is what is meant by the term _finite impulse response_. 
If the impulse response has 0 support for all n<0, it is causal. During convolution, all future values will be irrelevant. 
The order of an FIR filter of length N = M+1 is "M" (more covered in chapter 6). When order M is also the total number of delay elements, the filter is said to be canonical with respect to delay.  

## Transient Response, State, Decay

![[Pasted image 20230511145027.png]]
![[Pasted image 20230511145109.png]]

For a filter of length N, it takes N-1 steps to warm up to a steady state.

### Definition of Transients, Steady State, Decay
A mathematically convenient definition is as follows: A signal is said to contain a _transient_ whenever its Fourier expansion requires an _infinite_ number of [sinusoids](https://ccrma.stanford.edu/~jos/mdft/Sinusoids.html). Conversely, any signal expressible as a _finite_ number of [sinusoids](https://ccrma.stanford.edu/~jos/mdft/Sinusoids_Exponentials.html) can be defined as a _steady-state signal_. Thus, waveform discontinuities are transients, as are discontinuities in the waveform slope, curvature, etc. Any fixed sum of sinusoids, on the other hand, is a steady-state signal.

In speech, vowels and sibilants (ssss) can be viewed as steady states, while short consonants are transients. In music percussion and plucks are transients. Decay is identical to transients but time-shifted. Decay is calculated via the filter's internal state. 

## Signal flow graphs
See chapter 9.  
https://ccrma.stanford.edu/~jos/filters/Signal_Flow_Graph_I.html
https://ccrma.stanford.edu/~jos/filters/Direct_Form_II.html


## Further reading
Physical modeling book: https://ccrma.stanford.edu/~jos/pasp/Finite_Difference_Schemes.html

## Questions
When convolving two functions/signals which do not have a non-zero value until time t, does it take 2t timesteps before we see a non-negative value? 