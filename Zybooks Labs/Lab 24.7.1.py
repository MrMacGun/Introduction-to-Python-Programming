#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/7
uint1 = int(input())
uint2 = int(input())
uint3 = int(input())

ulist = [uint1, uint2, uint3]
minval = min(ulist)
maxval = max(ulist)

for i in ulist:
    if i != minval and i != maxval:
        print(i)