# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:40:16 2019

@author: hamza
"""

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums


def sample_long_running_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw'

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # The language of the supplied audio
    language_code = "ur-PK"
    audio_channel_count=2

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
        "audio_channel_count": audio_channel_count,

    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))


sample_long_running_recognize("gs://osaru_bucket/11Faiz Ahmad Faiz reads his own Poetry -(Remembering the legend).flac")