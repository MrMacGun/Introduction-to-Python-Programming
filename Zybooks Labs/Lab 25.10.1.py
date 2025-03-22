# Step 3: Input the arrow head width and ensure it's larger than the arrow base width.

# Input arrow base height and width
base_height = int(input())  # arrow base height
base_width = int(input())   # arrow base width

# Ensure the arrow head width is larger than the base width
while True:
    head_width = int(input())  # arrow head width
    if head_width > base_width:
        break  # Exit loop if the condition is met

# Draw the rectangle (arrow base)
for i in range(base_height):
    print('*' * base_width)  # Print '*' base_width times for each row

# Draw the right triangle (arrow head)
for i in range(head_width, 0, -1):  # Start from head_width and reduce by 1 each row
    print('*' * i)  # Print '*' i times for each row