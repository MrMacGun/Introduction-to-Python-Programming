#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/8

newlsit = []
uint = ''

while True:
    uint = input()
    if uint == '*':
        break
    else:
        newlsit.append(uint)

for i in reversed(newlsit):
    print(i, end=',')

print("")