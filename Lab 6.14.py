#This lab is to print the Reverse Binary? of each given input
#Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in reverse binary
#I.E. Input 6 output is 011
#input must be greater than 0, output as x mod 2 and then assign x with x divided by 2

num1 = int(6)

while num1 > 0:
    print(num1 % 2, end = '')
    num1 = num1//2

print("")

