#This program is intended to solve an equation using brute force only
#The equation will deduce var(x) + var(y) = anw & var(x) - var(y) =anw
# Lab reference https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/6/section/16

#''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

#''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

def function_main(a, b, c, d, e, f):
    solution = False

    for x in range(-10, 11):
        for y in range(-10, 11):

            if (a*x+b*y) == c and (d*x+e*y) == f:
                solution = True
                print(f"x = {x}, y = {y}")
                break

        if solution:
            False
            print("There is no solution")
            break

    if not solution:
        print("There is no solution")

