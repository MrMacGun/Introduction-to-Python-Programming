filename = input("Enter a file: ")

# Initialize the dictionary with letter counts set to 0
letters_dict = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
    'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 
    'y': 0, 'z': 0
}

# Read the file and convert all characters to lowercase
with open(filename, 'r') as file:
    # Read the entire content of the file
    content = file.read().lower()  # Convert content to lowercase

# Count each letter's occurrences
for letter in content:
    if letter in letters_dict:
        letters_dict[letter] += 1

# Print the dictionary showing letter counts
print(letters_dict)
