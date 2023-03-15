#!/usr/local/bin/python
# -*- coding: utf8 -*-
# -*- coding: ascii -*-
#from __future__ import unicode_literals
#By Azar Hosseini,2014.

import sys, csv, re , os,urllib,difflib,string,cv2,urlparse,glob
from bs4 import BeautifulSoup
import urllib2,logging, traceback
from urllib2 import HTTPError,URLError
from os.path import basename
from hazm import Normalizer
from hazm import sent_tokenize, word_tokenize
import BeautifulSoup,nltk,time,string
import urlparse,HTMLParser
from BeautifulSoup import BeautifulSoup
import time,webbrowser
from PIL import ImageGrab
from scipy.spatial import distance as dist
import numpy as np
from os.path import basename
import os, errno
from PIL import Image
import requests  
from lxml import html  
import sys  
import urlparse
import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import numpy as np
import matplotlib.pyplot as plt 
import cv2
import os
import urllib2


TargetPath="C:/Users/x/Downloads/fwprogram/important-sites-list.txt"
site_file=open(TargetPath,'r')
TARGET=[]
for row in site_file:
    s=row.split('\n')
    TARGET.append(s[0])

for eleman in TARGET:
    
    try:
        #EXAMPLE FOR similars_to_Domain_PATH: "C:/Python27/Phishing_CSIRT_93/bmi_similars_list.txt"
        words_gathered = open ("c://Python27/Phishing_CSIRT/outputs/%s_TotalWords.txt"%eleman,"a+")
        #site1-common-word
        h0="http://%s"%eleman
        req0=urllib2.Request(h0)
        #print h0
        try:
            response0 = urllib2.urlopen(req0)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                words_gathered.write(h0)
                words_gathered.write('We failed to reach a server.')
                words_gathered.write('Reason: %s'%e.reason)
                print h0
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                words_gathered.write(h0)
                words_gathered.write('The server couldn\'t fulfill the request.')
                words_gathered.write('Error code: %s'%e.code)
                print h0
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
        else:
            try:
                
                sock1=urllib.urlopen("http://%s"%eleman)
                l="http://%s"%eleman
                htmlsource1=sock1.read()
                fars1=re.sub('[!^a-zA-Z0-9{}<>-_."=/://;#--()|]','',htmlsource1)
                fars2=fars1.strip()
                fars3=fars1.split()
                fars4="  ".join(fars3)
                s2=str(fars4)
                soup = BeautifulSoup(s2)
                get=soup.getText()
                o=word_tokenize(get)
                o1=sorted(set(o))
                words_gathered.write(o1)
                for e in range(len(o1)):
                    print >> words_gathered , o1[e].encode("UTF-8")
            except:
                pass

