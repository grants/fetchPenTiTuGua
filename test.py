#!/usr/bin/python
# -*- coding: utf-8 -*-
# python
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import requests
import os
import re
import random
import socket
socket.setdefaulttimeout(10)
number=random.randint(106600,106700)
url="http://dapenti.com/blog/more.asp?name=tupian&id="+str(number)
try:
	webpagesrc=urlopen(url).read()
	uhtml=unicode(webpagesrc,"gbk")
	soup=BeautifulSoup(uhtml)
	srcend=soup.originalEncoding
	ps=soup.findAll('p')
	for p in ps:
		imgp=p.find("img")
		if (imgp):
			break
		else:
			continue
	if (imgp):
		imgsrc=imgp['src']
		downloadpicpath="~/camp/pentitugua/"+str(number)+".jpg"
		if os.path.exists(downloadpicpath):
			pass
		else:
			os.system("wget "+imgsrc+" -qO "+downloadpicpath+
					" && convert -resize 300 "+downloadpicpath+" "+downloadpicpath)
			#thetext=textp.renderContents()
		print "------------------------------------------------------------------"
		os.system("tycat "+downloadpicpath)
		#showtext=re.sub("&nbsp;","",re.sub("<[^>]*?>","",thetext))
		#show=""
		#for s in showtext.splitlines():
		#	s=s.rstrip()
		#	show+=s
		#print show
		print "------------------------------------------------------------------"
	else:
		print "nothing find"
except Exception,e:
	print e

