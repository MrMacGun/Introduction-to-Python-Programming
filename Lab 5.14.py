#Lab 5.14
#Interstate Highway Numbers https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/5/section/14
#This lab is supposed to take an input of a number and output which type of highway it is (Either primary or alternate)
#Then this program will give the direction of the highway along with an invalid input text

# User enters a number and it outputs a highway number
highway_number = int(input())
prim = 'is primary,'
aux = 'is auxiliary,'
serv = highway_number % 100

if highway_number >= 1 and highway_number <=99:
    if highway_number % 2 == 0:
        print('I-' + str(highway_number), prim, 'going east/west.')
    else:
        print('I-' + str(highway_number), prim, 'going north/south.')
elif highway_number >= 100 and highway_number <= 999:
    if highway_number % 100 == 0:
        print(highway_number, 'is not a valid interstate highway number.')
    elif highway_number % 2 == 0:
        print('I-' + str(highway_number), aux, 'serving I-{}, going east/west.'.format(serv))
    else:
        print('I-' + str(highway_number), aux, 'serving I-{}, going north/south.'.format(serv))
else:
    highway_number <= 0 and highway_number >= 1000
    print(highway_number, 'is not a valid interstate highway number.')

