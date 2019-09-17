# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:20:17 2019

@author: hamza
"""

#creating this to extract Audios with their Scripts.


import urllib.request as ur

from bs4 import BeautifulSoup

response = ur.urlopen('http://www.bbc.co.uk/worldservice/learningenglish/081222_download.shtml')
doc  = response.read()
soup = BeautifulSoup(doc,'html.parser')
links = soup.find_all( 'a' )  #p is an array of all hyperlink tags
#print(links)

for link in links : # Processing each link and getting the url value
    url = link.get( 'href' )
    if '.mp3' or '.pdf' in url and str(type(url)).equals('str'):
        #print(url)
        try:
            res = ur.urlopen(url)
            
            header = res.info()
            print(header)
            if res.info()['Content-Type']=='audio/mpeg' or res.info()['Content-Type']=='application/pdf':
                #filename = res.info()['Content-Disposition'] . split( '=' )[-1] . strip( '"' )
                #filename = ur.unquote(filename)
                urlsplit=url.split('/')
                #print(urlsplit[-1])
                #print(res,header)
                data = res.read()
                #print(data)
                with open( urlsplit[-1], "wb" ) as code:
                    code.write(data)

        except  ValueError as e:
            print(e)


'''

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