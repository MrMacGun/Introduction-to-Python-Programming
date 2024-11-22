#https://codingbat.com/prob/p197466
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
    if n%21 < 21:
        n = 21 - n
        return n
    elif n%21 > 21:
        n = (21 - n) * 2
        return n

print('Enter an interger and the program will calcualte the absoulte difference')
print(diff21(int(input())))

