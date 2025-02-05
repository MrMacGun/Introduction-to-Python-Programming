#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/5

print("Enter desired auto service:")
autoserve = input()

if autoserve == "Oil change":
    print(f'You entered: {autoserve}')
    print("Cost of oil change: $35")
elif autoserve == "Tire rotation":
    print(f'You entered: {autoserve}')
    print('Cost of tire rotation: $19')
elif autoserve == "Car wash":
    print(f'You entered: {autoserve}')
    print("Cost of car wash: $7")
else:
    print(f'You entered: {autoserve}')
    print("Error: Requested service is not recognized")
