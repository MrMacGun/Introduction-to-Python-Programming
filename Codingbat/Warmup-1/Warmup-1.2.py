#https://codingbat.com/prob/p120546
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling
#We are in trouble if they are both smiling or if neither of them is smiling.
#Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    elif weekday == False and vaction == True:
        return False
    else:
        return False

print("Type True if both of the monkeys are smiling or False for each one that isn't")
print("In fact these are chimps, if they're both smiling or both not smiling you'll end up on reddit")
print(sleep_in(str(input()), str(input())))