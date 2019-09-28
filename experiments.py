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


import os
from textteaser import TextTeaser
tt = TextTeaser()
text = os.read("F:\\Current Semester\\FYP\\OASRU\\ResultScripts\\45 MINT   01 03 2019-N_F_-9Z12Ew_Female_44100_CLEAN6.wav")
tt.summarize("PTV 45 mins",text)







