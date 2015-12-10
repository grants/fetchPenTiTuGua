# -*- coding: utf-8 -*-
# python
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
webpagesrc=urlopen("http://dev.tordian.net:10001").read()
parser=BeautifulSoup(webpagesrc)
print parser
