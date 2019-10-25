# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 08:51:13 2019

@author: hamza
"""
# working
'''

import os
lis = os.listdir('D:\\UrduDataset\\NEWSPROGRAM\PTV45Minutes\\ResultAudio\\')
lis.sort(key=lambda x: os.stat(os.path.join('D:\\UrduDataset\\NEWSPROGRAM\PTV45Minutes\\ResultAudio\\', x)).st_mtime)
print(lis)
'''

# not working
'''

import textract as te
import os 
import docx2txt
directroy = 'F:\\Current Semester\\FYP\\OASRU\\ResultScripts\\'
alllist = os.listdir(directroy)
text = ''
for each in alllist:
    if each.endswith(".zip"):
        my_text = docx2txt.process(directroy+each)
        print(my_text) 
'''

#Testing'

#from gensim.summarization.summarizer import summarize

#print(summarize(""))


#file= open(',"a+",encoding="utf-8")
#text = file.read()


from urduhack.stop_words import STOP_WORDS

for each in STOP_WORDS:
    print(each)
f = open('F:\\Current Semester\\FYP\\OASRU\\1.doc', 'r',encoding="utf-8")
txt = f.read()

'''
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('urdu'))

print(stop_words)
'''
import os
import speech_recognition as sr
import time

r = sr.Recognizer()


