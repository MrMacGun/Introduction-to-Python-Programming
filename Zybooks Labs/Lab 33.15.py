#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/15
#Write a program to read dates from input, one date per line. 
#Each date's format must be as follows: March 1, 1990. Any date not following that format is incorrect and should be ignored.

month_to_number = {'January':1 , 'Febuary': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
userstr = ""


def string_manipulation(userstr):
    while True:
        userstr = input()
        
        # Split the input string into parts
        parts = userstr.split()
        
        if len(parts) == 3 and parts[1][-1] == ',' and parts[0] in month_to_number:
            # Extract the month, day, and year from the input
            month = parts[0]
            day = int(parts[1][:-1])  # Remove the comma and convert to integer
            year = int(parts[2])
            
            # Output the date in correct format
            print(f"{month_to_number[month]}/{day}/{year}")
       
print(string_manipulation)


