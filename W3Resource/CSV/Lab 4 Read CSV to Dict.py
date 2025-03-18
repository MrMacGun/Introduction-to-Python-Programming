#https://www.w3resource.com/python-exercises/csv/index.php

import csv

filename = 'test.csv'

with open(filename, 'r', newline='') as file:
    newfile = csv.reader(file)
    for row in newfile:
        print(row)
        