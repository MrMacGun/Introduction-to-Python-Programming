#https://codingbat.com/prob/p189616
#Count Evens
#Return the number of even ints in the given array

nums = input()
num_list = [int(num) for num in nums.split()]

def count_evens(num_list):
    count = 0 
    for i in num_list:
        if i % 2 == 0:
            count += 1
    print(count)


count_evens(num_list)