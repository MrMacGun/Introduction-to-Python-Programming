#https://codingbat.com/prob/p116620
#Given 2 ints, a and b, return their sum.
#However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sorta_sum(a, b):
    sumnum = a + b
    if sumnum < 9:
        return sumnum
    elif (sumnum >= 10) and (sumnum <= 19):
        return 20
    elif sumnum >= 20:
        return sumnum

print("enter two numbers a and b seperated via the enter key")
print("both numbers will be added tother EXCEPT if it's in between 10 and 19, then it's only 20")
print(sorta_sum((int(input())), (int(input()))))