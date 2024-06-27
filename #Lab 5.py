#Lab 5.16 Leap Year
#Program will take an input that calculates if it is or is not a leap year
#Year must be divisable by 4

is_leap_year = False

input_year = int(1900)

if input_year  % 400 == 0 and input_year % 100 != 0:
    print(f"{input_year}- leap year")

elif input_year % 4 == 0 and input_year % 100 != 0:
    print(f"{input_year}- leap year")

else:
    print(f"{input_year}- not a leap year")
