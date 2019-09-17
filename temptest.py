# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:20:17 2019

@author: hamza
"""

#creating this to extract Audios with their Scripts.


import urllib.request as ur
import urllib.error as er

from bs4 import BeautifulSoup

#response = ur.urlopen('http://www.bbc.co.uk/worldservice/learningenglish/081222_download.shtml')
#response = ur.urlopen('http://www.radio.gov.pk/16-02-2018/audio-bulletin-1100-hours-16-02-2018')
#response = ur.urlopen('http://www.radio.gov.pk/programs')
audiobulletinbase = 'http://www.radio.gov.pk/audio-bulletin'
base = 'http://www.radio.gov.pk'
response = ur.urlopen(audiobulletinbase)


doc  = response.read()
soup = BeautifulSoup(doc,'html.parser')
links = soup.find_all( 'a' )  #p is an array of all hyperlink tags
#print(links)

for link in links : # Processing each link and getting the url value
    url = link.get( 'href' )
    print(url)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    #print(base+url)
    innerurl = base+url
    try:
        
        innerresponse = ur.urlopen(innerurl)
        innerdoc = innerresponse.read()
        innersoup= BeautifulSoup(innerdoc,'html.parser')
        innerlinks = innersoup.find_all('a')
        for innerlink in innerlinks:
            innerurl = innerlink.get('href')
            print(innerurl)
    except Exception as e:
        print(e)
    except TypeError as e:
        print(e)
'''
        try:
            res = ur.urlopen(innerurl)
            
            header = res.info()
            print(header)
        except  ValueError as e:
            print(e)
        except er.URLError as e:
            print(e)

'''

'''
for link in links:
    url = link.get( 'href' )
    mp3s = soup.find_all( '.mp3' )
    for mp3 in mp3s:      #Processing each link and getting the url value
        filename = mp3.get( 'src' )
        print(filename)
        data = ur.urlopen(filename).read()
        with open( "myfile.mp3", "wb" ) as code :
            code.write( data )

'''