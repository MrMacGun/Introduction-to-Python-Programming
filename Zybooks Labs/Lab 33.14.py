#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/14
#Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

def str_change(userstr):
    userstr = userstr.replace(" ", "").lower()
    if userstr == userstr[::-1]:
        return True
    else:
        return False

userstr = str(input())

if str_change(userstr) == True:
    print(userstr, "is a palindrome")
elif str_change(userstr) == False:
    print(userstr, "is not a palindrome")
