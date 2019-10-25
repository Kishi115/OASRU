# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:16:22 2019

@author: hamza
"""
import pandas as pd
import pydub as pdb
from pydub import AudioSegment
import os
import time

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
'''
 https://github.com/ina-foss/inaSpeechSegmenter 
CNN-based audio segmentation toolkit. Allows to detect speech, music 
and speaker gender. Has been designed for large scale gender equality 
studies based on speech time per gender. 
'''
'''

'''

# maintain a list for timetaken by every audio segmented in from the InDirectory
timelistdf = pd.DataFrame()
filelist = []
timelist = []
audiolength = []
from inaSpeechSegmenter import Segmenter, seg2csv
InDirectory = 'F:\\Current Semester\\FYP\\OASRU\\UrduStudioGrade\\'
#InDirectory = 'D:\\UrduDataset\\NEWSPROGRAM\PTV45Minutes\\'
#InDirectory = 'F:\\VoiceRecognition\\Foresight_research\\Ogni4Zubair'
# please specify your file and directory here
for WavFile in os.listdir(InDirectory):
    
    if WavFile.endswith(".flac"):
        
        # segmentation process started 
        starttime = time.time()
        print(WavFile)
        FileName= WavFile
        
        # Please specify your output directory here

        #OutDirectory = 'F:\\vr\\UrduVoiceRecognitionGit\\SegmentationOutputAudio\\'        
        #OutDirectory = 'D:\\UrduDataset\\NEWSPROGRAM\PTV45Minutes\\ResultAudio\\result'+FileName+'\\'
        OutDirectory = 'F:\\Current Semester\\FYP\\OASRU\\ResultAudio\\result'+FileName+'\\'
        ensure_dir(OutDirectory)
        #>>>>>>> 69b37757d3d7ad06c578e9f6937b996582272a98
        
        # Your Media path
        Media= InDirectory+'\\'+FileName
        print('Media:'+Media)
        # Segmenter Object
        segmenter = Segmenter()
        
        '''
        Audio = AudioSegment.from_wav(Media) 
        print(Audio.frame_rate,
        Audio.channels,
        Audio.DEFAULT_CODECS,
        Audio.frame_width,
        Audio.channels,
        Audio.dBFS,
        Audio.max_dBFS)
        '''
        
        # Returns a list of tuples with segment information eg, ('Male',0.92,3)
        print('Segmenting ...')
        SegmentInfoTupleList= segmenter(Media)
        
        print('segments done')
        seg2csv(SegmentInfoTupleList, OutDirectory+
                FileName[:len(FileName)-5]+
                'AudioSegmentation.csv')
        # File to be segmented into pydub.audio_segment.AudioSegment
        
        # Iterate over tuples in the list
        for tupl in SegmentInfoTupleList[:]:
            if tupl[0] not in ('Male','Female', 'NOACTIVITY'):
                print('deleting')
                SegmentInfoTupleList.remove(tupl)
        
        seg2csv(SegmentInfoTupleList, OutDirectory+
                FileName[:len(FileName)-5]+
                'AudioSegmentation_Cleaned.csv')
        '''
        #Incase you want to know about your audio file
        
        print(Audio.frame_rate,
        Audio.channels,
        Audio.DEFAULT_CODECS,
        Audio.frame_width,
        Audio.channels,
        Audio.dBFS,
        Audio.max_dBFS)
            
        '''
        Audio = AudioSegment.from_file(Media)
        
        # Initialize result and part with empty pydub.audio_segment.AudioSegment
        Result= AudioSegment.silent() 
        Part = AudioSegment.silent()
        
        # Frame rate to str
        AudioFrameRate = str(Audio.frame_rate)
        tag='NULL'
        
        # Compiling result
        for i, info in enumerate(SegmentInfoTupleList):
            #info[0] is tag 
            #info[1] is starting point of segment
            #info[2] is ending point of segment
            if(info[0]!=tag and info[0]!='NOACTIVITY'):
                tag=info[0]    
            print('Slicing...')
            Part = Part + Audio[((info[1])*1000):((info[2])*1000)]
            if(Part.duration_seconds>=20):
                print(Part.duration_seconds,'Exporting Segment ',i)
                Part.export(OutDirectory+FileName[:len(FileName)-5]+'_'+tag+'_'
                                                    +AudioFrameRate+
                                                    '_CLEAN{0}.flac'.format(i),
                                                    format='flac')
                Part = AudioSegment.silent()
                
        print(Part.duration_seconds,'Exporting Segment ',i)
        Part.export(OutDirectory+FileName[:len(FileName)-5]+'_'+tag+'_'
                                                    +AudioFrameRate+
                                                    '_CLEAN{0}.flac'.format(i),
                                                    format='flac')   
        endtime = time.time()
        audiolength.append(len(Audio)/1000)
        filelist.append(FileName)
        timelist.append(endtime-starttime)
        starttime=0
        endtime=0
        #timelist=[]

timelistdf['filename']=filelist
timelistdf['timetaken']=timelist 
timelistdf['length']=audiolength


timelistdf.to_csv('F:\\Current Semester\\FYP\\OASRU\\ResultAudio\\'+
'TimeListv1.csv')