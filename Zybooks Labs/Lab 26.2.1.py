#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/2

def max_magnitude(x, y, z):
    if abs(x) >= abs(y) and abs(x) >= abs(z):
        return x
    elif abs(y) >= abs(x) and abs(y) >= abs(z):
        return y
    else:
        return z

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())

    print(max_magnitude(x, y, z))