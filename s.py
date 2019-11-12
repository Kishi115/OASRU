# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:15:32 2019

@author: hamza
"""
import os
from jiwer import wer
from nltk.tokenize import RegexpTokenizer
import time
from urduhack import urdu_characters as urch
import pandas as pd

urap = urch.URDU_ALPHABETS
urpunc = urch.URDU_PUNCTUATIONS

path = 'F:\\Current Semester\\FYP\\OASRU\\UrduText\\'
textdir = (os.listdir(path))
traintext= ''
testtext =''

#testdir = textdir[7:]



for each in textdir:
    if not(each.startswith('~')):
        f=open(path+each,encoding="utf-8")
        traintext+=f.read()
    f.close()



#start_words = []
end_words = []
tokenizer = RegexpTokenizer(r'\w+')
traintokens_without_punctuation = tokenizer.tokenize(traintext)
traintokens_with_punctuation = traintext.split(" ")

my = ['۔']
punctuations = []
for each in traintokens_with_punctuation:
    if each not in traintokens_without_punctuation:
        punc =each[len(each)-1:]
        if  punc not in punctuations and punc not in urap and punc in my:
            punctuations.append(each)

punctuations = ' '.join([str(elem) for elem in punctuations])
punctuations = punctuations.replace("۔"," ")
punctuations = punctuations.split(" ")

testtextpath = "F:\Current Semester\FYP\OASRU\\Summary\\"

for file in os.listdir(testtextpath):
    if file.endswith(".doc") and '45' in file:
        print(file)
        f=open(testtextpath+file,encoding="utf-8")
        testtext+=f.read()
    f.close()


testtokens = testtext.split(" ")

i = 0
for word in testtokens:
    if word in punctuations:
        testtokens[i]=word+"۔"
    i+=1

punctuatedresult = ' '.join([str(elem) for elem in testtokens])


f= open("F:\Current Semester\FYP\OASRU\\ResultScripts\\"+"45_punctuated"+".doc","a+",encoding="utf-8")
f.write(punctuatedresult)
f.close()
#punctuations = list(pd.unique(punctuations))
       
from urduhack import stop_words as stopwords
from urduhack import stop_words

sentences = punctuatedresult.split("۔")
from summa import summarizer

summary=(summarizer.summarize(punctuatedresult,language="english",additional_stopwords=stopwords.STOP_WORDS))
print(len(summary))
print(len(punctuatedresult))

f= open("F:\Current Semester\FYP\OASRU\\ResultScripts\\"+"45_punctuated_summarized"+".doc","a+",encoding="utf-8")
f.write(summary)
f.close()
'''
# Extract word vectors
word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()
'''
'''
#USING TEXT-SUMMARIZER
import text_summarizer
from text_summarizer import summarizer

# Init summarizer parameters
summarizer.text = punctuatedresult
summarizer.algo = Summ.TEXT_RANK    # Summ.TEXT_RANK is equals to "textrank"
summarizer.percentage = 0.25

# Summarize with summarize() (returns a paragraph) or schematize() (returns a schema)
summarizer.summarize()
summarizer.schematize()

# You can also init the parameters in the summarize() / schematize() call
summarizer.summarize(text_to_be_summarized)
summarizer.summarize(text_to_be_summarized, "textrank", 0.5)
'''
'''
stopWords = stop_words.STOP_WORDS
words = punctuatedresult.split(" ")
words = ' '.join([str(elem) for elem in words])
words = words.replace("۔"," ")
words = words.split()

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
        

sentences = punctuatedresult.split("۔")
for each in sentences:
    if len(each)<13:
        sentences.remove(each)

sentenceValue = dict()
for sentence in sentences:
    for wordValue in freqTable:
        
        if len(wordValue)>1:
            print(wordValue[1])
            if wordValue[0] in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence]+= wordValue[1]
                else:
                    sentenceValue[sentence] = wordValue[1]
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))

summary = ''
for sentence in sentences:
        if sentence in sentenceValue and sentenceValue[sentence] > (1.5 * average):
            summary +=  " " + sentence
'''

'''
i = 0
while i<len(list_text)-1:
    word = list_text[i]
    if word.endswith("۔"):
        word = word[:len(word)-1]
        #print(i)
        if(word not in end_words):
            #print(word)
            end_words.append(word)
        #if(word not in start_words):
            #print(list_text[i+1])
            #start_words.append(list_text[i+1])
    i+=1

#newtext=testtext.replace("۔"," ")


newlist_text = tokens
word = ""

i=0
while i<len(newlist_text)-3:
    word = newlist_text[i]
    if end_words.__contains__(word) and word in ' '.join([str(elem) for elem in newlist_text[i:i+3]])  :
        #print('endword')
        newlist_text[i]=word+"۔"
    i+=1

segmentedtext = ' '.join([str(elem) for elem in newlist_text])

exportpath='F:\\Current Semester\\FYP\\OASRU\\UrduText\\'
name = 'seg'

f= open(exportpath+name+".doc","a+",encoding="utf-8")
f.write(segmentedtext)
f.close

error = wer(testtext, segmentedtext)
print(error)

'''


