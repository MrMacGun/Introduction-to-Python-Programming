#Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". 
#Each file contains two rows of comma-separated values
#Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. 
#Output the file contents as two dictionaries.
#The solution output should be in the format {'key': 'value', 'key': 'value', 'key': 'value'}
import csv

filename = input()

with open(filename, 'r') as f:
    line = csv.reader(f)
    for l in line:
        temp_list = [x.replace(' ', '') for x in l]
        dictionary = zip(temp_list[::2], temp_list[1::2])
        print(dict(dictionary))

