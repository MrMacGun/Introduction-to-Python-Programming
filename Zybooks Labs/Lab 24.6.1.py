#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/6
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

print("Select first service:")
Serv1 = input()
print("Select second service:\n")
Serv2 = input()
Total1 = 0
Total2 = 0

print("Davy's auto shop invoice\n")
if Serv1 == 'Oil change':
    print(f'Service 1: {Serv1}, $35')
    Total1 = 35
elif Serv1 == "Tire rotation":
    print(f'Service 1: {Serv1}, $19')
    Total1 = 19
elif Serv1 == "Car wash":
    print(f'Service 1: {Serv1}, $7')
    Total1 = 7
elif Serv1 == "Car wax":
    print(f'Service 1: {Serv1}, $12')
    Total1 = 12
elif Serv1 == "-":
    print("Service 1: No service")

if Serv2 == 'Oil change':
    print(f'Service 2: {Serv2}, $35\n')
    Total2 = 35
elif Serv2 == "Tire rotation":
    print(f'Service 2: {Serv2}, $19\n')
    Total2 = 19
elif Serv2 == "Car wash":
    print(f'Service 2: {Serv2}, $7\n')
    Total2 = 7
elif Serv2 == "Car wax":
    print(f'Service 2: {Serv2}, $12\n')
    Total2 = 12
elif Serv2 == "-":
    print("Service 2: No service\n")

Ftotal = Total1 + Total2
print(f'Total: ${Ftotal}')

