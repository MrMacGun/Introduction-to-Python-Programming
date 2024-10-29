#Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". 
#Each file contains two rows of comma-separated values
#Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. 
#Output the file contents as two dictionaries.
#The solution output should be in the format {'key': 'value', 'key': 'value', 'key': 'value'}
import csv

file_name1 = input()

if file_name1 is True:
    with open(file_name1.txt) as f:
        fn1r1 = str(f.readline().strip)
        fn1r2 = str(f.readline().strip)

if file_name2 is True:
    with open(file_name2.txt) as f:
        fn2r1 = str(f.readline().strip)
        fn2r2 = str(f.readline().strip)

print(f"{fn1r1}{fn1r2}")
