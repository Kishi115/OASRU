# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:38:52 2019

@author: hamza
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:55:32 2019

@author: hamza
"""


import os
import speech_recognition as sr
import time

# r is Speech Recognition Recognizer object
r = sr.Recognizer()
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
# the directroy having segments you want to script are
# eg 'drive:\\ProjectFolder\\SegmentedAudios\\'
InputDirectory = "D:\\UrduDataset\\NEWSPROGRAM\PTV45Minutes\\ResultAudio\\result45 MINT   01 03 2019-N_F_-9Z12Ew.wav\\"

# the directory to save script to 
ScriptDirectory = "F:\Current Semester\FYP\OASRU\ResultScripts\\result45 MINT   01 03 2019-N_F_-9Z12Ew.wav\\"

ensure_dir(ScriptDirectory)
   
# please put the name of file which you segmented before e.g PM_IK , Sample1


files = os.listdir(InputDirectory)
files.sort(key=lambda x: os.stat(os.path.join(InputDirectory, x)).st_mtime)
    
#iterating over Directory
resultlist = []
firstname = []


for filename in files:
    if (filename.endswith(".wav")):
        print(" Start Recognizing")
        x= filename.split('_')
        soundbite = sr.AudioFile(InputDirectory+filename) 
        with soundbite as source:
            #r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            r.adjust_for_ambient_noise(source)
            r.__reduce__
        try:
            text = r.recognize_google(audio, language="EN-PK")
            tmp = tuple([text,x[0]])
            resultlist.append(tmp)
            # output text file create         
            
            OutputFile= open(ScriptDirectory+filename+".doc","a+",encoding="utf-8")
            # recognized text in variable text
            text = r.recognize_google(audio, language="ur-PK")
            print(text)
            print(" Writing")
            OutputFile.write(text+"\n")
                  
            print('Done!')
            time.sleep(2)
            
            #close file
            # Empty the text variable
            text=""
        except Exception as e:
            
            # Incase there is some undefined behaviour
            print("There is some issue with:",filename)
            print (e)
        continue
    else:
        print('doing nothing')
        continue
