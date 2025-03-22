#Program deletes negative values and reorganizes the list from smallest to largest
user_int = input('Enter Numbers with spaces:')

elements = []

for i in user_int.split():
    elements.append(int(i))

for elements in elements:
    if int < 0:
        elements.pop()

print(elements.sort)
