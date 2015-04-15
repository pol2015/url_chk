import urllib2
from BeautifulSoup import BeautifulSoup
import csv
from urlparse import urlparse
import httplib
import socket
import requests
#import urlparse
import ie_title_check

from splinter.request_handler.status_code import HttpResponseError

from splinter import Browser
browser = Browser('firefox')
#browser = Browser('chrome')
from time import sleep
import winsound
import time
Freq = 2000 # Set Frequency To 2500 Hertz
Dur = 500 # Set Duration To 1000 ms == 1 second

#browser = Browser('chrome')
#browser = Browser('firefox')
#browser = Browser('zope.testbrowser')
#url = 'http://www.uol.com.br'
#url2 = 'http://www.cnn.com'


#browser.visit(url)
#print browser.status_code.code 
#winsound.Beep(Freq,Dur)
#print url
#print browser.title

#time.sleep(5)
#winsound.Beep(Freq,Dur)
#browser.visit(url2)
#print browser.title
#print url2
#browser.quit()




#ie_title_check.main('www.cnn.com')
#input_url3.csv

out_file = open("C:\Users\-6\py_data\url_chk\output_url4.csv", "ab")
in_file = open("C:\Users\-6\py_data\url_chk\input_url4.csv","rb")

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
            item[2] = browser.title
            print item[2]
            winsound.Beep(Freq,Dur/2)
            out_data=csv.writer(out_file)
            out_data.writerow(item)
            
            out_file.close
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

        except UnicodeEncodeError:
            pass
            item[2] = 'Unicode Error'
            printingresulterror()

            
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
