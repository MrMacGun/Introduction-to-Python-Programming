#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/4

def days_in_feb(user_year):
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return 29
    else:
        return 28

if __name__ == '__main__':
    year = int(input())
    print(f'{year} has {days_in_feb(year)} days in February.')