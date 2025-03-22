#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/7
n = int(input())

# Initialize a counter to keep track of how many numbers have been printed in the current line
count = 0

# While n is not 1, generate the hailstone sequence
while n != 1:
    print(n, end='\t')  # Print the current number followed by a tab
    count += 1
    
    if count == 10:  # If we printed 10 numbers, start a new line
        print()  # Print a newline
        count = 0  # Reset the counter
    
    # Apply the hailstone rule
    if n % 2 == 0:
        n = n // 2  # If n is even, divide by 2
    else:
        n = 3 * n + 1  # If n is odd, multiply by 3 and add 1

# Print the final 1 to end the sequence
print(n)


    