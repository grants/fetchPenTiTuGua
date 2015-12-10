# -*- coding: utf-8 -*-
# python
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import requests
import os
import re
number=106633
url="http://dapenti.com/blog/more.asp?name=tupian&id="+str(number)
webpagesrc=urlopen(url).read()
uhtml=unicode(webpagesrc,"gbk")
soup=BeautifulSoup(uhtml)
srcend=soup.originalEncoding
ps=soup.findAll('p')
imgp=ps[2].find("img")
textp=ps[3]
imgsrc=imgp['src']
downloadpicpath="~/camp/pentitugua/"+str(number)+".jpg"
if os.path.exists(downloadpicpath):
	pass
else:
	os.system("wget "+imgsrc+" -qO "+downloadpicpath+" && convert -resize 300 "+downloadpicpath+" "+downloadpicpath)
thetext=textp.renderContents()
print "------------------------------------------------------------------"
os.system("tycat "+downloadpicpath)
showtext=re.sub("&nbsp;","",re.sub("<[^>]*?>","",thetext))
show=""
for s in showtext.splitlines():
	s=s.rstrip()
	show+=s
print show
print "------------------------------------------------------------------"
