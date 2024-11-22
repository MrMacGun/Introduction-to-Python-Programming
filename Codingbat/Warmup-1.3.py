def sum_double(a, b):
    if a == b:
        return ((a+b)*2)
    else:
        return a+b

print("Enter two number, only two you stingy basterd. The numbers will be added togther")
print("If the numbers are the same, the sum will be doubled")
print(sum_double((int(input())), int(input())))
