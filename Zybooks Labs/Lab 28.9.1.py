#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/9

uint = input()
new_list = list(map(int, uint.split(" ")))

threshold = new_list [-1]
output = []

for i in new_list[:-1]:
    if i <= threshold:
        output.append(str(i))

print(",".join(output), end=',')
print("")