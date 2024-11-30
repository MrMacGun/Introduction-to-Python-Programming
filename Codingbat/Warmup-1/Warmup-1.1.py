#https://codingbat.com/prob/p173401
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if weekday == False and vacation == False:
        return True
    elif weekday == True and vacation == False:
        return False
    elif weekday == False and vaction == True:
        return True
    else:
        return True

print("Is it true that is it is a weekday? And is it true is it a weekend?")
print("Type True or False twice to both questions and this program will determine if you're allowed to sleep in")
print(sleep_in(str(input()), str(input())))