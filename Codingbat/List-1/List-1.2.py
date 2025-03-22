#https://codingbat.com/prob/p179078
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
    return len(nums) > 1 and nums[0] == nums[-1]

print("Enter a set of numbers seperated via spaces, if the first and last number is equal *Note* must be more than one number")
input_str = input()
numsarray = list(map(int, input_str.split()))

print(same_first_last(numsarray))