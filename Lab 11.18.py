#Code outputs the numbers in a given list that is inbetween 0 and 50

input_list = int(input())

list_nums = [int(i) for i in input_list.split]

for i in list_nums:
    if i in list_nums not in range(0, 50):
        list_nums.pop

print (list_nums)
