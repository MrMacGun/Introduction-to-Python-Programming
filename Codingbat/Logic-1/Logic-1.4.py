#https://codingbat.com/prob/p137202
#You are driving a little too fast, and a police officer stops you
#Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
#If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
#Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    points = 0
    if is_birthday == True:
        if speed in range(35, 65):
            points += 1
            return points
        elif speed in range(66, 85):
            points += 2
            return points
        elif speed >= 86:
            points += 3
            return points
    elif is_birthday != True:
        if speed in range(30, 65):
            points += 1
            return points
        elif speed in range(61, 80):
            points += 2
            return points
        elif speed >= 81:
            points += 3
            return points

print("12 Caught ya ass, how was was you goin fam?")
speed = int(input())
print("Also they lettin you off easy today, if it was your birthday (and it was), say true or false")
is_birthday = bool(input())

print(caught_speeding(speed, is_birthday))

