#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/13

height = int(input())

for i in range(height):
    print(' ' * (height - i - 1), end='')
    print('* ' * i)
