# Code takes two inputs as a string. Name and last 7 digits of a phone number *including dashes
#Then when a user inputs a name *Must match case and spelling* and outputs the last 7 with dashes
#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/11/section/19

name_7num = str(input('Input First Name'), input('Phone # last 7, with dash'))

contactlist = []

for i in name_7num:
    contactlist.append(name_7num)

userq = str(input('Input First Name'))

if userq in contactlist:
    print 