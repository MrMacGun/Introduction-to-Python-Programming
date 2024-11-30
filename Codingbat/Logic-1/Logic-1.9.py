#https://codingbat.com/prob/p165321
#Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
#Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. 

def near_ten(num):
    num = mun % 2
    if num > 8:
        return True

print("Enter a number, if the number mod 2 is close to 2 the program is true")
userint = int(input())

print(near_ten(userint))