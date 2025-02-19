#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/1

def laps_to_miles(laps):
    miles = laps * .25
    return miles

if __name__ == '__main__':
    laps = float(input())
    print(f'{laps_to_miles(laps):.2f}')