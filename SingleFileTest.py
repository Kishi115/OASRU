import os
import speech_recognition as sr
import time


# r is Speech Recognition Recognizer object
r = sr.Recognizer()

# the directroy having segments you want to script are
InputDirectory = "F:\\vr\\UrduVoiceRecognitionGit\\SegmentationOutputAudio"

# the directory to save script to 
ScriptDirectory = "F:\\vr\\UrduVoiceRecognitionGit\\RecognizerOutputText"

# please put the name of file which you segmented before e.g PM_IK , Sample1
InputFile='Sample1'



#iterating over Directory
for filename in os.listdir(InputDirectory):
    if (filename.endswith(".wav") and filename.startswith(InputFile)):
        print(" Start Recognizing")
        soundbite = sr.AudioFile(InputDirectory+filename) 
        with soundbite as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
        try:
            # output text file open
            OutputFile= open(InputFile+".txt","w+",encoding="utf-8")
            text = r.recognize_google(audio, language="ur-PK", show_all=False)
            print(" Writing ")
            print (text)
            OutputFile.write(text+"\n")
            time.sleep(2)
            OutputFile.close()
            text=""
        except Exception as e:
            print("There is some issue with:",filename)
            print (e)
        continue
    else:
        continue 