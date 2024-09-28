#Code has a a built in pre-defined list
#User inputs a number between 0-6 to output the element type within the list

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

user_index = int(input("Enter a number between 1-5 to see the class of an element within a list: "))

element = various_data_types[user_index]
print(f'Element {user_index}: {type(element).__name__} ')