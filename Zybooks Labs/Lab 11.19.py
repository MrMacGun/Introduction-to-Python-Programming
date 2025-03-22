# Code takes two inputs as a string. Name and last 7 digits of a phone number *including dashes
#Then when a user inputs a name *Must match case and spelling* and outputs the last 7 with dashes
#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/11/section/19

info = input().split(' ')  #takes string and separates by space
contacts = {}   #empty dictionary 

for i in info:  #iterating over info list
    split = i.split(',') 
    contacts[split[0]] = split[1]  #creating the key, value pairs
    
name = input()   #asks which name to search
print(contacts[name])  #prints value associated with key