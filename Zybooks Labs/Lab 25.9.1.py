# (1) Take the user input for the character and triangle height
triangle_char = input("Enter a character:\n")
triangle_height = int(input("Enter triangle height:\n"))
print("")

# (2) Use a loop to draw the right triangle
for i in range(1, triangle_height + 1):  # Loop through each line of the triangle
    # Print the specified character 'i' times, each followed by a space
    print((triangle_char + ' ') * i)
