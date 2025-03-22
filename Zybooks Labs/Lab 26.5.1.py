#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/5
def exact_change(change):
    if change <= 0:
        print("no change")
        return None, None, None, None  
    num_quarters = change // 25
    change %= 25  
    num_dimes = change // 10
    change %= 10  
    num_nickels = change // 5
    change %= 5  

    num_pennies = change

    if num_pennies > 0:
        print(f"{num_pennies} penny{'ies' if num_pennies > 1 else ''}")
    if num_nickels > 0:
        print(f"{num_nickels} nickel{'s' if num_nickels > 1 else ''}")
    if num_dimes > 0:
        print(f"{num_dimes} dime{'s' if num_dimes > 1 else ''}")
    if num_quarters > 0:
        print(f"{num_quarters} quarter{'s' if num_quarters > 1 else ''}")

    return num_pennies, num_nickels, num_dimes, num_quarters  # Return the results

if __name__ == '__main__':
    user_input = int(input()) 
    exact_change(user_input)
