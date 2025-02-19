#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/7
def count_evens(num1, num2, num3, num4):
    count = 0 
    if num1 % 2 == 0:
        count += 1
    if num2 % 2 == 0:
        count += 1
    if num3 % 2 == 0:
        count += 1
    if num4 % 2 == 0:
        count += 1
        
    return count

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    
    result = count_evens(num1, num2, num3, num4)
    print('Total evens:', result)