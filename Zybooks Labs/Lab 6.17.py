#This lab is intended to adjust a list of integers 2 decimal places back
#If the integer is less than 1 after division, it is discarded

num_values = int(input())

# Initialize an empty list to store the values
values = []

# Read the floating-point values and store them in the list
for _ in range(num_values):
    value = float(input())
    values.append(value)

# Find the largest value in the list
max_value = max(values)

# Normalize each value and print it formatted to two decimal places
for value in values:
    normalized_value = value / max_value
    print(f'{normalized_value:.2f}')


