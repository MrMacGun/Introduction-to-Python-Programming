#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/12

a = (float(input("Enter weight 1:\n")))
b = (float(input("Enter weight 2:\n")))
c = (float(input("Enter weight 3:\n")))
d = (float(input("Enter weight 4:\n")))

new_list = [a, b, c, d]
print("Weights:", new_list)
print("")
total = 0
for i in new_list:
    total = total + i

average = total / 4
print(f"Average weight: {average:.2f}")
print(f"Max weight: {max(new_list):.2f}")
print("")
index_input = int(input("Enter a list location (1 - 4):"))
new_var = new_list[index_input - 1]
print("")
print(f"Weight in pounds: {new_var:.2f}")
kilos = new_var / 2.2
print(f'Weight in kilograms: {kilos:.2f}')
new_list.sort()
print("")
print("Sorted list:", new_list)