#https://www.w3resource.com/python-exercises/csv/index.php

import csv

filename = 'test.csv'

with open (filename, 'r') as file:
    new_file = csv.reader(file)
    for row in new_file:
        print(row)

