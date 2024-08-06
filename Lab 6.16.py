#This program is intended to solve an equation using brute force only
#The equation will deduce var(x) + var(y) = anw & var(x) - var(y) =anw
# Lab reference https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/6/section/16

#''' Read in first equation, ax + by = c '''
a = int(8)
b = int(7)
c = int(38)

#''' Read in second equation, dx + ey = f '''
d = int(3)
e = int(-5)
f = int(-1)

# Initialize solution variables
check = False

for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if a * x + b * y == c and d * x + e * y == f:
            check = True
            print(f"x = {x} , y = {y}")

if check == False:
    print('There is no solution')