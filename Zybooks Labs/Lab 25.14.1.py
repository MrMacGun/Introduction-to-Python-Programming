#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/14

# Get the input for the height of the triangle
height = int(input())

# Loop through the height in reverse order
for i in range(height, 0, -1):
    # Print '*' i times, followed by a space
    print('* ' * i)
