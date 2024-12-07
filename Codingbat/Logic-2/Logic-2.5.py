#https://codingbat.com/prob/p179960
#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
#Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
#Given 3 ints, a b c, return the sum of their rounded values.
#To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    # Get the last digit using modulo operation
    last_digit = num % 10
    if last_digit >= 5:
        # Round up to the next multiple of 10
        return num + (10 - last_digit)
    else:
        # Round down to the previous multiple of 10
        return num - last_digit
    
print("Enter a set of three number, they will be rouneded up or down bases on the nearest 10")
print(round_sum(int(input()), int(input()), int(input())))