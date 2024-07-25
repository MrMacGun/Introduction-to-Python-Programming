#This lab is to print the Reverse Binary? of each given input
#Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in reverse binary
#I.E. Input 6 output is 011
#input must be greater than 0, output as x mod 2 and then assign x with x divided by 2

value = input(int())
if value <= 0:
        raise ValueError("Input must be a positive integer")

    binary_digits = []
    while value > 0:
        remainder = value % 2
        binary_digits.append(str(remainder))
        value //= 2

    # Join the list of binary digits and reverse the string
    value = ''.join(binary_digits)[::-1]
    return value

# Example usage:
try:
    num = int(input("Enter a positive integer: "))
    reversed_binary = reverse_binary(num)
    print(f"Reverse binary representation: {reversed_binary}")
except ValueError as e:
    print(e)

