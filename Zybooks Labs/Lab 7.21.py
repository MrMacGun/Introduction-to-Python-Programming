def int_to_reverse_binary(usernum):
    while usernum > 0:
        x = usernum % 2
        x = x // 2
        return str(x)

def string_reverse(x = str()):
    return reversed(x)

if __name__ == '__main__':
    usernum = int(input())
    print(f"{int_to_reverse_binary(string_reverse)}")