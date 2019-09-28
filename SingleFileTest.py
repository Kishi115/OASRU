import os
import speech_recognition as sr
import time


# r is Speech Recognition Recognizer object
r = sr.Recognizer()


# please put the name of file which you segmented before e.g PM_IK , Sample1
dire ='F:\\Current Semester\\FYP\\OASRU\\ResultAudio\\result140918_6min_london_skyline_for_web_140918_6min_london_skyline_audio_au_bb.wav\\'
dirlist=os.listdir(dire)
for filename in dirlist:

    if filename.endswith('.wav'):
        print(filename)
        print(" Start Recognizing")
        soundbite = sr.AudioFile(dire+filename) 
        with soundbite as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 100
            r.non_speaking_duration =1
            r.dynamic_energy_threshold = False
            audio = r.record(source)
        try:
            # output text file open
            text = r.recognize_google(audio, language="EN-UK", show_all=False)
            print(" Writing ")
            print (text)
            time.sleep(2)
            break
        except Exception as e:
            print("There is some issue with:")
            print (e)
            
