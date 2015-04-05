import urllib2
from BeautifulSoup import BeautifulSoup
import csv
from urlparse import urlparse
import httplib
import socket


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
     print "error here"

     out_data=csv.writer(out_file)
     out_data.writerow(item)
     out_file.close


def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()

    return resp.status

for item in getdata(in_data):


#for index,item in enumerate(data):
    if __name__ == '__main__':
        try:                   
            print item[0]
            item[1] = checkUrl(item[0])
            print item[1]
            soup = BeautifulSoup(urllib2.urlopen(item[0]))
            item[2] = soup.title.string
            print item[2]
            out_data=csv.writer(out_file)
            out_data.writerow(item)
            out_file.close
            
        except socket.gaierror:
            pass
            item[1] = 'False'
            item[2] = 'socket.gaierror'
            printingresulterror()
            
        except urllib2.HTTPError:
            pass
            item[2] = 'HTTPError'
            printingresulterror()
        except AttributeError:
            pass
            item[2] = 'Attribute Error'
            printingresulterror()
        except UnicodeEncodeError:
            pass
            item[2] = 'Unicode Error'
            printingresulterror()
        except socket.error:
            pass
            item[2] = 'socket.error '
            printingresulterror()

        except urllib2.URLError:
            pass
            item[2] = 'urllib2.URLError   '
            printingresulterror()
             
        except httplib.BadStatusLine:
            pass
            item[2] = 'httplib.BadStatusLine  '
            printingresulterror()


        except httplib.HTTPException:
            pass
            item[2] = 'socket.error '
            printingresulterror()

     
   
 






