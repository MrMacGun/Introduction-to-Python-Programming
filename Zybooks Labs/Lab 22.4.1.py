#Given two numbers that represent the lengths of a right triangle's legs (sides adjacent to the right angle)
#Output the length of the third side (i.e. hypotenuse) with two digits after the decimal point.

import math

a = float(input())
b = float(input())

c = math.sqrt((a * a) + (b * b))

print(f'Hypotenuse: {c:.2f}')