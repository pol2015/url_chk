# -*- coding: utf-8 -*-

import sys

print sys.stdout.encoding


import urllib2
from BeautifulSoup import BeautifulSoup
import csv
from urlparse import urlparse
import httplib
import socket
import requests
#import urlparse
import ie_title_check
import unicodecsv
from cStringIO import StringIO
f = StringIO()

import codecs
import sys 
UTF8Writer = codecs.getwriter('utf8')

from splinter.request_handler.status_code import HttpResponseError

from splinter import Browser
browser = Browser('firefox')
#browser = Browser('chrome')
from time import sleep
import winsound
import time
Freq = 2000 # Set Frequency To 2500 Hertz
Dur = 500 # Set Duration To 1000 ms == 1 second

#sys.stdout.encoding="utf-8"

out_file = open("C:\Users\-6\py_data\url_chk\output_url8.csv", "ab")
in_file = open("C:\Users\-6\py_data\url_chk\input_url8.csv","rb")

in_data=csv.reader(in_file)

soup=[1,2,3,4,5,6]


def getstuff(filename):
    with in_file as csvfile:
        data=csv.reader(in_file)
        count = 0
        for row in data:
            yield row
            count += 1
     

def getdata(filename):
        for row in getstuff(filename):
            yield row


def printingresulterror():
     print item[2]

     out_data=csv.writer(out_file)
     out_data.writerow(item)
     out_file.close
     
#w = unicodecsv.writer(f, encoding='utf-8')

for item in getdata(in_data):

    if __name__ == '__main__':
        try:                   
            print item[0]
            url = item[0]
            #print ie_title_check.main(item[0])
            #item[4] = ie_title_check.main(item[0])
            #item[1] = checkUrl(item[0])
            browser.visit(url)
            #winsound.Beep(Freq,Dur)
            item[1] = browser.status_code.code
            print item[1]
            item[2] = browser.title.encode(sys.stdout.encoding, errors='replace')
            x = browser.title
            #y = x
            #sys.stdout = UTF8Writer(sys.stdout)
            #print y
            #print u"Stöcker".encode(sys.stdout.encoding, errors='replace')
            #print u"Стоескер".encode(sys.stdout.encoding, errors='replace')
            print x.encode(sys.stdout.encoding, errors='replace')
            print type(x)
            #y = (x.encode('utf-16'))
            #print y
            #print type(y)
            #print item[2]
            winsound.Beep(Freq,Dur/2)

            out_data=csv.writer(out_file)
            out_data.writerow(item)
            out_file.close
            #out_data=unicodecsv.writer(out_file, encoding='utf-8')
            #out_data.writerow(item)
            
            #out_file.close
            winsound.Beep(Freq*2,Dur)
           
            
        except socket.gaierror:
            pass
            item[1] = 'False'
            item[2] = 'socket.gaierror'
            printingresulterror()



        except HttpResponseError:
            pass
            item[1] = 'False'
            item[2] = 'HttpResponseError'
            printingresulterror()



            
##            
##        except urllib2.HTTPError:
##            pass
##            item[2] = 'HTTPError'
##            printingresulterror()
##            
##        except AttributeError:
##            pass
##            item[2] = 'Attribute Error'
##            printingresulterror()
##

##        except UnicodeEncodeError:
##            pass
##            item[2] = 'Unicode Error'
##            printingresulterror()

            
        except socket.error:
            pass
            item[2] = 'socket.error '
            printingresulterror()

            
##
##        except urllib2.URLError:
##            pass
##            item[2] = 'urllib2.URLError   '
##            printingresulterror()
##             
##        except httplib.BadStatusLine:
##            pass
##            item[2] = 'httplib.BadStatusLine  '
##            printingresulterror()
##
##
##        except httplib.HTTPException:
##            pass
##            item[2] = 'socket.error '
##            printingresulterror()
