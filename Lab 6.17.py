#This lab is intended to adjust a list of integers 2 decimal places back
#If the integer is less than 1 after division, it is discarded

usernum = 0 

while usernum > 0: 
    usernum = float(input())
    usernum/100
    if usernum > .01: 
        print(f'{usernum:.2f}')
    else:
        usernum.remove()
        continue
