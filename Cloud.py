# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:18:33 2019

@author: hamza
"""


import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

#135Nafsani Khuwaishat Chorne Per Jannat  Mufti Taqi Usmani Sahab.mp4
# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname("F:\\Current Semester\\FYP\\CloudAudio\\"),
    '04Faiz Ahmed Faiz - Nisar Main Teri Galiyon Kay Ae Watan By ARaziq Piracha.flac'
    )

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    language_code='ur-PK')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))