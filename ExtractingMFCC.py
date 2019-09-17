# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:35:36 2019

@author: hamza
"""

from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
directory = "F:\\Downloads\\musan\\noise\\"
(rate,sig) = wav.read("noise-free-sound-0000.wav")
mfcc_feat = mfcc(sig,rate)
d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])