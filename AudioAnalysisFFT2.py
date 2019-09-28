
import matplotlib.pyplot as plt
from scipy.fftpack import fft , ifft
from pylab import*
from scipy.io import wavfile # get the api
import os
import pandas as pd
import librosa
import glob
import librosa.display
#fs, data = wavfile.read('..\\OriginalAudios\\test3_M.wav') # load the data
data, fs = librosa.load('..\\urdu-voice-recognition\\OriginalAudios\\PM_IK.wav')

print(fs)
print(data)
data = data / (2.**15)
timeArray = arange(0, data.shape[0], 1)
timeArray = timeArray / fs
#timeArray = timeArray * 1000  #scale to milliseconds
'''
plt.plot(timeArray, data, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')

'''
n = len(data) 
p = fft(data) # take the fourier transform 
nUniquePts = int(ceil((n+1)/2.0))
p = p[0:nUniquePts]
p = abs(p)

p = p / float(n) # scale by the number of points so that
                 # the magnitude does not depend on the length 
                 # of the signal or on its sampling frequency  
#p = p**2  # square it to get the power 

# multiply by two (see technical document for details)
# odd nfft excludes Nyquist point
if n % 2 > 0: # we've got odd number of points fft
    p[1:len(p)] = p[1:len(p)] * 2
else:
    p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft
plt.figure(figsize=(20, 4))

freqArray = arange(0, nUniquePts, 1.0) * (fs / n);
plt.plot(freqArray/1000, 10*log10(p), color='k')
xlabel('Frequency (kHz)')
ylabel('Power (dB)')
