import urllib2
from BeautifulSoup import BeautifulSoup
import csv

out_file = open("C:\Users\-6\py_data\url_chk\output_url.csv", "wb")
in_file = open("C:\Users\-6\py_data\url_chk\input_url.csv","rb")

data=csv.reader(in_file)
out_data=csv.writer(out_file)

soup=[]

data = [row for row in csv.reader(in_file) ]



for index,item in enumerate(data):
    soup = BeautifulSoup(urllib2.urlopen(item[0]))
    print soup.title.string
    item[1] = soup.title.string

for item in data:
    out_data.writerow(item)
    
out_file.close()
