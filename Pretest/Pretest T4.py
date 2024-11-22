#Program takes three integers to output the area of a Trapezoid

Base1 = float(input())
Base2 = float(input())
Height = float(input())

Area = ((Base1 * Base2 / 2)) * Height

print(f'Trapezoid area: {Area:.1f} square meters')
