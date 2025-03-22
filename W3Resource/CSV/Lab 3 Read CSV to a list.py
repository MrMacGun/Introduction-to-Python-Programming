#https://www.w3resource.com/python-exercises/csv/index.php
import csv

filename = 'test.csv'
newlist = []

with open (filename, 'r') as file:
    ucsv = csv.reader(file)
    for row in file:
        newlist.append(row)

for x in newlist:
    print(x)

