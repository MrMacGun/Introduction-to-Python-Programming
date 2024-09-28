input_list = input(int())

list_nums = [int(i) for i in input_list.split() if 0 <= int(i) <= 50]

print(' '.join(map(str, list_nums)))