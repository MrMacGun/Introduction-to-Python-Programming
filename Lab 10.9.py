#Lab 10.9
#Write a program that removes all non-alpha(betic) characters from a given string

user_char = str(input())

filtered_char = ''.join(c for c in user_char if c.isalpha())

print(filtered_char)