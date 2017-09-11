import urllib2
import time
import re
from os.path import basename
from urlparse import urlsplit
import urllib
from BeautifulSoup import *
import os 
from downloader import *
import sys

print sys.argv
urlf=sys.argv[len(sys.argv)-1]
#raw_input("Enter URL: ")

if len(re.findall("^http://.+",urlf))<1:
	urlf="http://"+urlf
if len(re.findall("$/",urlf))>0:
	urlf=urlf[:len(urlf)-1]

f=urlf.split('/')
del f[3:]
v='/'
hos=v.join(f)
print 'host:', hos

q1='n'
#raw_input("Is it direct page of pics:(Y/N)")
if '-d' in sys.argv :
	print "====direct===="
	downloader(urlf, 'direct')
	exit()

d=f[len(f)-2]

print "The name of the essential folder is : ",d
try:
	os.mkdir(d)
	print "*********creating ",d," done**********"
except:
	pass
	print "folder is exist!"

hr=urllib.urlopen(urlf).read()
print "essential url read"
so=BeautifulSoup(hr)
tags0=so("a")
tags1=list()
for j in tags0:
	if j in tags1 :
		continue
	tags1.append(j)

time.sleep(20)
ccc='0'
print "tag completed and for begin"

for po in tags1 :
	
	print '\n',po
	url=po.get('href', None)
	url1='0'
	url1=re.findall("^/.+",url)
	if len(url1)>0:
		ccc=urlf+url1[0]
		
	url2=re.findall("^.*(http://.+)",url)
	if len(url2)>0:
		ccc=url2[0]
	
	sis='^'+hos+'.+'
	url3=re.findall(sis,url)
	if len(url3)>0:
		ccc=url3[0]
	if ccc != '0' :
		print "\n\n\n========",ccc,"======="
		q='0'
		qq=ccc.split('/')
		a=len(qq)
		q=d+'/'+qq[a-2]
		print "new sub folder ",q,"is creating..."
	
		try:
			os.mkdir(q)
			print "creating done"
		except:
			pass
			print "folder mybe exict"
		downloader(ccc,q)
		time.sleep(1)


