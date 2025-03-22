#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/23/section/1

fav_color = input()
fav_name = input()
unum = int(input())

print(f'You entered: {fav_color} {fav_name} {unum}\n')
first_pass = fav_color + "_" + fav_name
print(f'First password: {first_pass}')
sec_pass = str(unum) + fav_color + str(unum)
print(f'Second password: {sec_pass}\n')

num_char1 = len(first_pass)
num_char2 = len(sec_pass)

print(f'Number of characters in {first_pass}: {num_char1}')
print(f'Number of characters in {sec_pass}: {num_char2}')
