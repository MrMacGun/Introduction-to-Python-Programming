#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/11

loan = float(input())
payment = float(input())
interest = float(input())

count = 0 
while loan > 0:
    loan += loan * interest
    loan -= payment

    count += 1

if count == 1:
    print("1 payment")
else:
    print(f"{count} payments")