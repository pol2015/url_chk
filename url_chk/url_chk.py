import csv

out=open("data.csv","rb")
data=csv.reader(out)
data=[[row[0],eval(row[1]),eval(row[2])] for row in data]
out.close()

new_data=[[row[0],row[1]+row[2]] for row in data]

out=open("new_data.csv","wb")
output=csv.writer(out)

for row in new_data:
    output.writerow(row)

out.close()