#Using Heron's formula, you can calculate the area of a triangle if you know the lengths of all three sides.
#Given the length of each side of a triangle as input, calculate the area of the triangle using Heron's formula as follows:
#s = half of the triangle's perimeter
#area = the square root of s(s-a)(s-b)(s-c), where a, b, and c are each sides of the triangle.

import math

a = float(input())
b = float(input())
c = float(input())
s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f'The area of the triangle is: {area:.3f}')
