#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/1
Red = int(input())
Green = int(input())
Blue = int(input())
vallist = [Red, Green, Blue]
smallval = min(Red, Green, Blue)

Red = Red - smallval
Green = Green - smallval
Blue = Blue - smallval

print(Red, Green, Blue)
