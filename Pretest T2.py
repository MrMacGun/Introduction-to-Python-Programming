#Program takes a single input from the user as ounces
#Ounces are then divided up via tons, pounds and lastly onces 
#If the input is 32035 then the output is Tones: 1, Pounds: 2, Ounces: 3

user_int = int(input())

tons = user_int // 32000  # 1 ton = 32,000 ounces
remaining_ounces = user_int % 32000

pounds = remaining_ounces // 16  # 1 pound = 16 ounces
ounces = remaining_ounces % 16

print(f'Tons: {tons}')
print(f'Pounds: {pounds}') 
print(f'Ounces: {ounces}')
        



