import urllib2
from BeautifulSoup import BeautifulSoup
import csv
from urlparse import urlparse
import httplib
import socket

out_file = open("C:\Users\-6\py_data\url_chk\output_url2.csv", "wb")
in_file = open("C:\Users\-6\py_data\url_chk\input_url2.csv","rb")


data=csv.reader(in_file)
out_data=csv.writer(out_file)

soup=[1,2,3,4,5,6]


data = [row for row in csv.reader(in_file)  ]



def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400



for index,item in enumerate(data):

    if __name__ == '__main__':
        try:                   
            print item[0]
            item[1] = checkUrl(item[0])
            print item[1]
            soup = BeautifulSoup(urllib2.urlopen(item[0]))
            item[2] = soup.title.string
            print item[2]
        except socket.gaierror:
            pass
            item[1] = 'False'
        except urllib2.HTTPError:
            pass
            item[2] = 'HTTPError'
        except AttributeError:
            pass
            item[2] = 'Attribute Error'
        except UnicodeEncodeError:
            pass
            item[2] = 'Unicode Error'
        except socket.error:
            pass
            item[2] = 'socket.error '  

        except urllib2.URLError:
            pass
            item[2] = 'urllib2.URLError   '  
             
        except httplib.BadStatusLine:
            pass
            item[2] = 'httplib.BadStatusLine  '  

     
   
 
for item in data:
    out_data.writerow(item)

out_file.close()

#soup = BeautifulSoup(requests.get(url).text)
