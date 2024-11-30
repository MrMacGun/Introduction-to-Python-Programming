#https://codingbat.com/prob/p181624
#Given an array of ints, return True if 6 appears as either the first or last element in the array
#The array will be length 1 or more.

def first_last6(nums):
    # Check if the first or last element is 6
    return nums[0] == 6 or nums[-1] == 6

# Get user input
print("Enter a set of numbers separated by spaces, the program will check if the number 6 is at the beginning or end of the list.")
input_str = input()
numsarray = list(map(int, input_str.split()))

print(first_last6(numsarray))