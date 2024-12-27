#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/27/section/4

def remove_digits(user_string):
    # Remove all digits from the string using a list comprehension
    return ''.join([char for char in user_string if not char.isdigit()])

if __name__ == '__main__':
    # Read the input string
    user_string = input()
    
    # Call the remove_digits function and print the result
    print(remove_digits(user_string))
