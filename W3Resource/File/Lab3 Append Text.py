#https://www.w3resource.com/python-exercises/file/

filename = input("Enter a filename:")

with open(filename, "a") as file:
    newword = input("Enter Text")
    file.write(newword)

with open(filename, 'r') as file:
    firstline = file.readlines()
    print(firstline)