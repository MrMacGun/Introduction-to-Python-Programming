#https://codingbat.com/prob/p135815
#The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive).
#Unless it is summer, then the upper limit is 100 instead of 90. 
#Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
    play = True
    if temp in range(60, 90):
        return True
    elif (temp in range(60, 100)) and (is_summer == True):
        return True
    else:
        return False

print("Squireels like to play outside when it's betwen 60 and 90F")
print("If it's summer then they can play up to 100F (Doubtful)")
print("input the temprature followed by the enter key. Then input if it's summer via true or false")
temp = int(input())
is_summer = bool(input())

print(squirrel_play(temp, is_summer))