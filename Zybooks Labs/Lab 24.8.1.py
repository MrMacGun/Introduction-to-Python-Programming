#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/8

Speed_limit = int(input())
Car_speed = int(input())
Speed_Diff = Car_speed - Speed_limit
ticket = 0

if Speed_Diff == -10:
    ticket = 50
elif Speed_Diff in range(6, 21):
    ticket = 75
elif Speed_Diff in range(21, 41):
    ticket = 150
elif Speed_Diff > 40:
    ticket = 300

print(ticket)

