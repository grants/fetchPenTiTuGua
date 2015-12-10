# -*- coding: utf-8 -*-
# python
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import requests
url="http://dapenti.com/blog/more.asp?name=tupian&id=106633"
webpagesrc=urlopen(url).read()
uhtml=unicode(webpagesrc,"gbk")
soup=BeautifulSoup(uhtml)
srcend=soup.originalEncoding
ps=soup.findAll('p')
imgp=ps[2].find("img")
textp=ps[3]
imgsrc=imgp['src']
print imgsrc
thetext=textp.renderContents()
print thetext
