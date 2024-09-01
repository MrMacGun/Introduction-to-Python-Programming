def swap_values(num1, num2, num3, num4):
    return (num2, num1, num4, num3)

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    swap_values = swap_values(num1, num2, num3, num4)

    print(*swap_values)