#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/13

height = int(input())
for row in range(height):
    for s in range(height - row - 1):
        print(" ",end=' ')
    for a in range(row + 1):
        print('*', end=' ')
    print()
