#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/12

ustr = input()
char_match = input()

count = 0

length = min(len(ustr), len(char_match))

for i in range(length):
    if ustr[i] == char_match[i]:
        count += 1

if count == 1:
    print("1 character matches")
else:
    print(f'{count} characters match')

