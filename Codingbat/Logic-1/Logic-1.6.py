#https://codingbat.com/prob/p119867
#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation
#return a string of the form "7:00" indicating when the alarm clock should ring.
#Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
#Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
    # Weekdays: Monday to Friday (1 to 5)
    if day in range(1, 6):
        if vacation:
            return "10:00"  # On vacation, alarm time on weekdays is "10:00"
        else:
            return "7:00"  # Not on vacation, alarm time on weekdays is "7:00"
    
    # Weekends: Saturday (6) and Sunday (0)
    elif day == 6 or day == 0:
        if vacation:
            return "off"  # On vacation, no alarm on the weekend
        else:
            return "10:00"  # Not on vacation, alarm time on weekends is "10:00"

# Input part
print("Enter the day starting with Sunday(0), Monday(1), etc. followed by pressing Enter:")
day = int(input())

print("Enter true or false if it's a vacation and you will know when to set your alarm:")
vacation = input().lower() == 'true'  # Convert input string to boolean

# Output result
print(alarm_clock(day, vacation))