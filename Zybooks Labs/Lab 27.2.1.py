#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/27/section/2
char = input()

words = input().split()

for word in words:
    if char in word:
        print(word)
