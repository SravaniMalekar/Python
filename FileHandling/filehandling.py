##Opening a file in read mode 
buf=open('myFile.txt','r')
print(buf.read())

##Opening a file in write mode
buf=open('myFile.txt','w')
print(buf.write(0))

buf=open('myFile.txt','w')
print(buf.write('My File'))
buf.close()

buf=open('people.csv','rt')
buf.read()
buf.close()

with open('people.csv','rt')as buf:
    print(buf.read())
    buf.close()

import csv
##Reading a Csv file

with open('people.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open('people.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1:])
##Reading csv file row by row
buf=open('people.csv','r')
studs=[]
marks=[]

reader = csv.reader(buf)
next(reader,None)
for row in reader:
    studs.append(row[0])
    marks.append(row[2])


##Writing to a CSV file
import csv
sn=int(input('enter no'))
mn=input('enter movie')
r=int(input('enter rating'))
with open('protagonist.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["SN","Movie","Rating"])
    writer.writerow([1,"PK","3"])
    writer.writerow([1,"HarryPotter","5"])
    writer.writerow([sn,mn,r,'anything'])
    file.close()
