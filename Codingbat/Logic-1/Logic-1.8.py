#https://codingbat.com/prob/p158497
#Given a number n, return True if n is in the range 1..10, inclusive. 
#Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10

def in1to10(n, outside_mode):
  if (n in range(1, 10)) and (outside_mode == False):
    return True
  elif ((n <= 1) or (n >= 10)) and (outside_mode == True):
    return True
  else:
    return False

print("Enter a number and a a true or false value")
n = int(input())
outside_mode = bool(input())

print(in1to10(n, outside_mode))