# Input the three integers
low = int(input())  # low value
high = int(input())  # high value
x = int(input())  # the number whose multiples we're counting

# Initialize the count of multiples
count = 0

# Iterate over the range from low to high (inclusive)
for num in range(low, high + 1):
    if num % x == 0:  # If num is divisible by x
        count += 1

# Output the count of multiples
print(count)