#Program takes three integers to output the area of a Trapezoid

Base1 = int(input("Enter Base 1 of the Trapazoid: "))
Base2 = int(input("Enter Base 2 of the Trapazoid: "))
Height = int(input("Enter the Height of the trapazoid: "))

Area = ((Base1 * Base2 / 2)) * Height

print(f'Trapezoid area: {Area} square meters')