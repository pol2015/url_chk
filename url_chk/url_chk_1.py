import csv
import lxml.html


#t = lxml.html.parse(url)
#print t.find(".//title").text



out=open("C:\Users\-6\py_data\url_chk\input_url.csv","rb")

#data = [row for row in csv.reader(open('C:\Users\-6\py_data\url_chk\input_url.csv', 'rb'))]

data = [row for row in csv.reader(out)]

url = data[0][0]
        
data=csv.reader(out)



out.close()


#out=open("output_url.csv","wb")
#output=csv.writer(out)

#for row in new_data
#    output.writerow(row)

#out.close()

#OK

url5 = 'http://www.google.com'
t = lxml.html.parse(url5)
print t.find(".//title").text

