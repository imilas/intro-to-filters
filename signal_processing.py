import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import ellip, freqz, group_delay
from scipy import signal 
import matplotlib

def plot_freq_response(w, h):
    plt.subplot(211)
    plt.plot(w, np.abs(h))
    plt.title('Amp response')

    plt.subplot(212)
    plt.plot(w, np.angle(h))
    plt.title('Phase response')
    plt.tight_layout()
    
def plot_log_freq_response(b, a, title, ylim, fs=44100):
    w, H = signal.freqz (b, a, fs=fs)
    plt.figure()
    plt.semilogx (w, 20 * np.log10 (np.abs (H)))
    plt.title (title)
    plt.ylim (ylim)
    plt.gca().xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
    plt.xlabel ('Frequency [Hz]')
    plt.ylabel ('Magnitude [dB]')
    plt.xlim (20, 20000)
    
def interp_array(x):
    '''
    This can be used when DFT values contain NANs at 0 or nyquist
    '''
    xi = np.arange(len(x))
    mask = np.isfinite(x)
    xfiltered = np.interp(xi, xi[mask], x[mask])
    return xfiltered

def sinusoid_combo(freqs,coefs,l,sr=44100):
    '''
    f is a list of frequencies,
    c is the coefficient (or loudness) of said frequencies
    l is the length of output 
    '''
    a = np.zeros(l)

    for c,f in zip(coefs,freqs):
        a += c*np.sin(2*np.pi*f*np.linspace(0,1,sr,endpoint=False))
    
    return a 

def audio_spectrum(x):
    plt.plot(np.abs(np.fft.fft(x))[0:len(x)//2])
    
def filter_sound(sound,B,A,SR=44100):
    N_dft = np.fft.fft(sound) # dft of the sound
    w,h = signal.freqz(B,A,worN = SR,whole=True) # dft of the filter
    h = interp_array(h)
    output_dft = h*N_dft
    output = np.fft.ifft(output_dft)
    return output

def filter_noise(B,A,SR=44100,plot=True,):
    '''
    filter white noise with B,A parameters
    '''
    noise = np.random.normal(0,1,SR)
    output = filter_sound(noise,B,A,SR)
    if plot==True:
        plt.plot(np.abs(np.fft.fft(output))[0:len(output)//2])
    else:
        return output