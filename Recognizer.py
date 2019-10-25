# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:55:32 2019

@author: hamza
"""


import os
import speech_recognition as sr
import time
import pandas as pd
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# r is Speech Recognition Recognizer object
r = sr.Recognizer()

#chunks' directory
#chunksdir = 'D:\\UrduDataset\\TalkShow\\CapitalTalk'
chunksdir = 'F:\\Current Semester\\FYP\\OASRU\\ResultAudio'
# All folders in chunks' directroy

chunksdirlist = os.listdir(chunksdir)
chunksdirlist.sort(key=lambda x: os.stat(os.path.join(chunksdir, x)).st_mtime)
#transcripts' directory 
#scriptsdir = 'D:\\UrduDataset\\TalkShow\\CapitalTalk'
scriptsdir = 'F:\\Current Semester\\FYP\\OASRU\\ResultScripts\\'
ensure_dir(scriptsdir)
# All folders in scripts' directroy
#scriptdirlist = os.listdir(scriptdir)

# inner
chunkname = []
chunkrecognitiontime = []
chunklength = []

#outer
folderrecognitiontime = []
folderlength = []
foldername = []
for folder in chunksdirlist:
    print(folder)
    chunkfolderdir=chunksdir+'\\'+folder+'\\'
    if(os.path.isdir(chunkfolderdir)):
        
        foldername.append(folder)

        chunks_in_folder= sorted(os.listdir(chunkfolderdir), 
                           key=lambda x: os.path.getctime(os.path.join(chunkfolderdir, x)))
        OutputFile= open(scriptsdir+folder+".doc","w+",encoding="utf-8")
        OutputFile.close()
        #OutputFile = Document()
        #OutputFile.save(scriptsdir+folder+".docx")
        for InputFile in chunks_in_folder:
            
            if(InputFile.endswith('.flac')):
                starttime = time.time()
                chunkname.append(InputFile)    
                print(" Start Recognizing")
                soundbite = sr.AudioFile(chunkfolderdir+InputFile) 
                
                
                with soundbite as source:
                    #r.adjust_for_ambient_noise(source)
                    audio = r.record(source)
                    chunklength.append(soundbite.DURATION)
                    r.adjust_for_ambient_noise(source)
                    r.__reduce__
                try:
                    # output text file open
                    OutputFile= open(scriptsdir+folder+".doc","a+",encoding="utf-8")
                    # recognized text in variable text
                    text = r.recognize_google(audio, language="ur-PK")
                    print(text)
                    print(" Writing")
                    OutputFile.write(text+"\n")
                    #test= OutputFile.read()
                    #print('Testing: '+test)
                    print('Done!')
                    endtime = time.time()
                    chunkrecognitiontime.append(endtime-starttime)
                    time.sleep(0.5)
                    
                    #close file
                    OutputFile.close()
                    
                    # Empty the text variable
                    text=""
                except Exception as e:
                    chunkrecognitiontime.append(0)
                    # Incase there is some undefined behaviour
                    print("There is some issue with:",InputFile)
                    OutputFile.close()
                    print (e)
                continue
            OutputFile.close()
        innerdf = pd.DataFrame()
        innerdf['chunk'] = chunkname
        innerdf['length'] = chunklength
        innerdf['recognitiontime'] = chunkrecognitiontime
        innerdf.to_csv(scriptsdir+folder+'chunkList.csv')
        flen = sum(chunklength)
        frlen = sum(chunkrecognitiontime)
        folderlength.append(flen)
        folderrecognitiontime.append(frlen)
        chunklength = []
        chunkname = []
        chunkrecognitiontime = []
outerdf  = pd.DataFrame()        
outerdf['chunkfolder'] = foldername
outerdf['folderlength'] = folderlength
outerdf['recognitiontime'] = folderrecognitiontime
outerdf.to_csv(scriptsdir+folder+'folderList.csv')


        
        
        
        
        
        
        
    
    



'''
InputDirectory = ".\\"

# the directory to save script to 
ScriptDirectory = ".\\"

# please put the name of file which you segmented before e.g PM_IK , Sample1
InputFile='Muhammad Pervaiz (Peers of influence)Part-2._Female_8000_CLEAN34.wav'

OutputFile= open(InputFile+".doc","w+",encoding="utf-8")
OutputFile.close()
files = sorted(os.listdir(InputDirectory), 
               key=lambda x: os.path.getctime(os.path.join(InputDirectory, x)))

#iterating over Directory
for filename in files:
    if (filename.endswith(".wav") and filename.startswith(InputFile)):
        print(" Start Recognizing")
        soundbite = sr.AudioFile(InputDirectory+filename) 
        with soundbite as source:
            #r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            r.adjust_for_ambient_noise(source)
            r.__reduce__
        try:
            # output text file create
            
            
            OutputFile= open(InputFile+".doc","a+",encoding="utf-8")
            # recognized text in variable text
            text = r.recognize_google(audio, language="ur-PK")
            print(text)
            print(" Writing")
            OutputFile.write(text+"\n")
            
            print('Done!')
            time.sleep(2)
            
            #close file
            OutputFile.close()
            
            # Empty the text variable
            text=""
        except Exception as e:
            
            # Incase there is some undefined behaviour
            print("There is some issue with:",filename)
            print (e)
        continue
    else:
        OutputFile.close()
        continue
OutputFile.close()
'''