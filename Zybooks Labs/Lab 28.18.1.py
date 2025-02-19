#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/18

numbers = list(map(int, input().split())) 
N = int(input()) 

N = abs(N)

if len(numbers) < N:
    print(-N)
else:
    print(numbers[-N])

