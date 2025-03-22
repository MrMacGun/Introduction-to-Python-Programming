#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/3

def jiffies_to_seconds(seconds):
    jiffies = seconds * .01
    return jiffies

if __name__ == '__main__':
    seconds = float(input())
    print(f'{jiffies_to_seconds(seconds):.3f}')
