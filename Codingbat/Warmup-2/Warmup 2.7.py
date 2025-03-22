#https://codingbat.com/prob/p110166
#Given an array of ints, return True if one of the first 4 elements in the array is a 9
#The array length may be less than 4.
def arry_front9(nums):
    return 9 in nums

print("Input a set of numbers separated by spaces")
input_str = input()
arry_list = list(map(int, input_str.split()))
arry_slice4 = arry_list[:4]

print("The program will determine if 9 was within the first 4 elements")
print(arry_front9(arry_slice4))

