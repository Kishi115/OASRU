# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import youtube_dl
import os

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def my_hook(d):
    if d['status'] == 'finished':
        rcfvrprint('Done downloading, now converting ...')
ensure_dir('D:\\UrduDataset\\TalkShow\\CapitalTalk')


ydl_opts = {
    'format': 'bestaudio/best',
    'ignoreerrors': True,
    'outtmpl': 'D:\\UrduDataset\\TalkShow\\CapitalTalk\\%(title)s.%(ext)s' ,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
        
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
while(True):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            
            ydl.download(['https://www.youtube.com/playlist?list=PL82CE2B5363598982'])
        except Exception as e:
            print(e)
        continue
