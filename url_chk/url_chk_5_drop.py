import urllib2
from BeautifulSoup import BeautifulSoup
import csv
from urlparse import urlparse
import httplib
import socket
import requests
#import urlparse







out_file = open("C:\Users\-6\py_data\url_chk\output_url6.csv", "ab")
in_file = open("C:\Users\-6\py_data\url_chk\input_url6.csv","rb")


in_data=csv.reader(in_file)


soup=[1,2,3,4,5,6]


def resolve_http_redirect(url_test, depth=0):
    if depth > 10:
        raise Exception("Redirected "+depth+" times, giving up.")
    #o = urlparse.urlparse(url_test,allow_fragments=True)
    o = urlparse(url_test,allow_fragments=True)
    conn = httplib.HTTPConnection(o.netloc)
    path = o.path
    if o.query:
        path +='?'+o.query
    conn.request("HEAD", path)
    res = conn.getresponse()
    headers = dict(res.getheaders())
    if headers.has_key('location') and headers['location'] != url_test:
        return resolve_http_redirect(headers['location'], depth+1)
    else:
        return url_test
    
##url_test = "http://github.com"
##print url_test
##resolve_http_redirect(url_test, depth=0)
##print url_test
##print resolve_http_redirect(url_test)


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


def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()

    return resp.status
    #print resp.status

for item in getdata(in_data):


#for index,item in enumerate(data):
    if __name__ == '__main__':
        try:                   
            print item[0]
      
              
            
            item[1] = checkUrl(item[0])
            
            
            print item[1]
            soup = BeautifulSoup(urllib2.urlopen(item[0]))
            #item[2] = soup.title.string
            item[2] = soup.title
            #print soup.head
            resolve_http_redirect(item[0], depth=0)
            #print resolve_http_redirect(item[0])
            item[3] = resolve_http_redirect(item[0])


            
            #response = requests.get(item[0],allow_redirects=False
            #print response.status_code
            
            
#           print response
##            print "request"
##            print response.history
##            print response.url
##            if response.history:
##                print "Request was redirected"
##                for resp in response.history:
##                    print resp.status_code, resp.url
##                    print "Final destination:"
##                    print response.status_code, response.url
##            else:
##                    print "Request was not redirected"




            
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
            
        #except AttributeError:
        #    pass
        #    item[2] = 'Attribute Error'
        #    printingresulterror()


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

     
   
 






