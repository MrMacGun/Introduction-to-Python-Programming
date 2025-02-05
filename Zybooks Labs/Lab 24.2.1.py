#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/2

ustr1 = input()
ustr2 = input()

newustr1 = len(ustr1)
newustr2 = len(ustr2)

if newustr1 > newustr2:
    print(ustr1)
elif newustr1 == newustr2:
    print(ustr2)
elif newustr1 < newustr2:
    print(ustr2)