#Given the number of people attending a pizza party, output the number of needed pizzas and total cost.
#For the calculation, assume that people eat 2 slices on average and each pizza has 12 slices and costs $14.95.
#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/22/section/3

import math

uint = int(input())

num_slice = uint * 2
num_pies = math.ceil(num_slice / 12)

cost = num_pies * 14.95

print(f'Pizzas: {num_pies}')
print(f'Cost: ${cost:.2f}')