# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:15:48 2019

@author: muham
"""

from pydub import AudioSegment
import os 

    #directory = "SampleAudio"
#DIR with test files
# F:\\VoiceRecognition\\Foresight_research\\Ogni4Zubair\\Total
#directory = 'F:\\VoiceRecognition\\Foresight_research\\Ogni4Zubair'
directory = 'F:\Current Semester\FYP\OASRU\EnglishStudioGrade'

i = 0
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
          
        song = AudioSegment.from_file(directory+'\\'+filename)
        print("exporting "+filename.format(i))

        song.export(
                directory+'\\'+filename[:len(filename)-4]+'.wav'.format(i),
                format="wav")
        i = i+1
