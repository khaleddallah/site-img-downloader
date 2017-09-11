import urllib.request
import time
import re
from os.path import basename
#from urlparse import urlsplit
import urllib
from bs4 import BeautifulSoup
import os 
#import thread
'''
def wdget ( b ) :
	os.system(blah)
	continue
def ww (b) :
	time.sleep(55)
	continue
'''
def downloader (url,pat):
	if pat == "direct" :
		f=url.split('/')
		d=f[len(f)-2]
		
		try:
			os.mkdir(d)
			print ("creating done --direct--")
		except:
			pass
			print ("folder mybe exictd --direct--")
		pat=d	
	print ("===donwloding images in (",url,") to (",pat,")")
	try:
		hrd=urllib.request.urlopen(url).read()
		print ("reading---" , url , "---Done")
		sod=BeautifulSoup(hrd,"html.parser")
		tagsd=sod("a")
		
		
		for imgUrl in tagsd:
			try:
				imgUrl=imgUrl.get('href',None)
				print (imgUrl)
				
				#if  imgUrl.get('target',None)!="_blank":
				t1=re.findall('^.*.jpg',imgUrl)
				print ("test1 working ...")
				if len(t1)==0:
					print ('!!!!!! t1 failed !!!!!!')
					continue
				print ("test1 success.")
				
				
				"""
				t2=re.findall('^.*[0-9].jpg',imgUrl)
				print "test2 working ..."
				if len(t2)>0:
					continue
					print '!!!!!! t2 failed !!!!!!'
				
				t3u='^'+url+'.+'
				t3=re.findall(t3u,imgUrl)
				print t3
				print "test3 working ..."
				if len(t3)==0:
					imgUrl=url+imgUrl
					print "test3 success"
				"""
				print ("wslt lhon")	
				print ("\n.....downloading >>>" ,imgUrl)
				blah='wget -c --read-timeout=10 -P '+pat+' '+ imgUrl
				os.system(blah)
					
			except KeyboardInterrupt:
				break
			except:
				pass
	except:
		pass
	"\ndone\n\n"

