import urllib2
from BeautifulSoup import BeautifulSoup
import csv


out_file = open("C:\Users\-6\py_data\url_chk\output_url.csv", "wb")
in_file = open("C:\Users\-6\py_data\url_chk\input_url.csv","rb")


data=csv.reader(in_file)
out_data=csv.writer(out_file)

soup=[]
#print soup
#soup.append(7)
#soup.append(8)
#print soup

data = [row for row in csv.reader(in_file)  ]


#print data[0]
#print data[1]
#print data[2]
#print data[0][0]
#print data[1][0]
#print data[2][0]
#print row[0]

#print data[0][0]

#soup=BeatifulSoup(urllib2,urlopen(data[0][0]))
#print soup.title.string

row_count = len(data)

for index,item in enumerate(data):
    #print index+1
    #print item[0]
    soup = BeautifulSoup(urllib2.urlopen(item[0]))
    print soup.title.string
    item[1] = soup.title.string


#url = data[0][0]
#soup = BeautifulSoup(urllib2.urlopen(url))
#data [0][1] = soup.title.string
#print data[0][1]


#url = data[0][0]

#print data[0][1]

#soup = BeautifulSoup(urllib2.urlopen(url))
#print soup.title.string




for item in data:
    out_data.writerow(item)

out_file.close()

