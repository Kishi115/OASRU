# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:01:43 2019

@author: hamza
"""

"""
#requirnments
selenium
BeautifulSoup
pandas

"""

from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd



def BbcArticleScrapper(url,exportpath,name):

    driver = wd.Firefox()
    driver.get(url)
    
    #whole source
    content = driver.page_source
    
    # get set of tags in content
    soup = BeautifulSoup(content)
    
    # get required tag 
    src = soup.findAll('body')
    
    # get set of tags in raw text of src
    for each in src:
        insrc = each.findAll('div', attrs={'class':'direction'})
    #insrc = insoup.findAll('div')
    
    for each in insrc:
        in_insrc = each.findAll('div',attrs={"id":"orb-modules"})
    
    for each in in_insrc:
        req = each.findAll('div',attrs={"id":"site-container"})
    
    for each in req:
        in_req= each.findAll('div',attrs={"class":"configurable story"})
    
    
    for each in in_req:
        inreq= each.findAll('div',attrs={"role":"main"})
    
    
    for each in inreq:
        a= each.findAll('div',attrs={"class":"container"})
    
    for each in a:
        b= each.findAll('div',attrs={"class":"container--primary-and-secondary-columns column-clearfix"})
    
    for each in b:
        c= each.findAll('div',attrs={"class":"column--primary"})
    
    
    for each in b:
        c= each.findAll('div',attrs={"class":"story-body"})
    
    for each in c:
        title = each.findAll("h1")
        in_sb= each.findAll('div',attrs={"class":"story-body__inner"})
    
    for each in in_sb:
        intro = each.findAll("p",attrs={"class":"story-body__introduction"})
        paragraphs = each.findAll("p")
    
    title = title[0].text
    intro = intro[0].text
    body = ' '.join([elem.text for elem in paragraphs])
    driver.quit()
    
    article = title + "\n"+intro+"\n"+body    
    f= open(exportpath+name+".doc","a+",encoding="utf-8")
    f.write(article)
    f.close()


BbcArticleScrapper("https://www.bbc.com/urdu/pakistan-50258498",'F:\\Current Semester\\FYP\\OASRU\\UrduText\\','1')
