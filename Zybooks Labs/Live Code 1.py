#Given a List and a string in the list as paramters
#Write a function that return the index number where the string is found

user_list = ['Cow', 'Pig', 'Airplane', 'Mouse', 'Keyboard']


def outlist(user_list, user_input):
    if user_input in user_list:
        output = user_list.index(user_input)
        print(output)
    else:
        print("Error", user_input, "Not in List")


print("Enter a string")
user_input = 'Cow'
print(outlist(user_list, user_input))