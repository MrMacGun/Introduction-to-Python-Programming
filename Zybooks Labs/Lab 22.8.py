#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/22/section/8
# V = pi r^2 h
# A = 2pi r h + 2 pi r^2

import math

radius = float(input())
height = float(input())

volume = math.pi * math.pow(radius, 2) * height

surface_area = 2 * math.pi * radius * height + 2 * math.pi * math.pow(radius, 2)

print(f'Volume: {volume:.1f} cubic inches')
print(f'Surface area: {surface_area:.1f} square inches')
