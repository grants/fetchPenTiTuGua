#!/usr/bin/python
# -*- coding: utf-8 -*-
# python
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import requests
import os, errno
import re
import random
import socket

socket.setdefaulttimeout(30)

def mkdir_p(path):
	try:
		os.makedirs(path)
	except OSError as exc:
		if exc.errno==errno.EEXIST and os.path.isdir(path):
			pass
		else: raise

def shownews(number):
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
				textp=p.find("strong").parent
				break
			else:
				continue
		if (imgp):
			imgsrc=imgp['src']
			picturedir="/home/qihao/camp/pentitugua/picture"
			if not os.path.exists(picturedir):
				mkdir_p(picturedir)
			downloadpicpath=picturedir+"/"+str(number)+".jpg"
			sentencefile="/home/qihao/camp/pentitugua/sentence.txt"
			if os.path.exists(downloadpicpath):
				pass
			else:
				print "Downloading, please wait..."
				os.system("wget "+imgsrc+" -qO "+downloadpicpath+
						" && convert -resize 300 "+downloadpicpath+" "+downloadpicpath)
			thetext=textp.renderContents()
			print "------------------------------------------------------------------"
			os.system("tycat "+downloadpicpath)
			showtext=re.sub("&nbsp;","",re.sub("<[^>]*?>","",thetext))
			show=""
			for s in showtext.splitlines():
				s=s.rstrip()
				show+=s
			print show
			if (show!=""):
				sentenceToFile="["+str(number)+"] "+show+"\n"
				fp=open(sentencefile,'a+')
				fp.write(sentenceToFile)
				fp.close()
			print "------------------------------------------------------------------"
			return True
		else:
			print "nothing find"
			return False
	except Exception,e:
		print e
		return False

startNumber=input("Please input begin search url id number: ")
stopNumber=input("Pleaser input end search url id number: ")

for i in range(startNumber, stopNumber+1):
	ret=shownews(i)
	if ret:
		answer=raw_input("Next[y/n, defalut:y]? : ") or 'y'
		if (answer=='y'):
			continue
		else:
			os._exit(0)
	else:
		continue

os._exit(0)

