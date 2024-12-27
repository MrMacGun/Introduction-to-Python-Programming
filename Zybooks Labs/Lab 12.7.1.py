def get_age():
    try:
        age = int(input())
        # Check if age is within the valid range (18 to 75 inclusive)
        if 18 <= age <= 75:
            return age
        else:
            print("Invalid age.")
            print("Could not calculate heart rate info.")
            return None
    except ValueError:
        print("Invalid age.")
        print("Could not calculate heart rate info.")
        return None

def fat_burning_heart_rate(age):
    if age is None:
        return None  # Return None if age is invalid
    else:
        heart_rate = (220 - age) * 0.70
        return heart_rate

if __name__ == "__main__":
    age = get_age()  # Get age from user input
    if age :  # If age is valid (not False)
        heart_rate = fat_burning_heart_rate(age)
        if heart_rate is not None:
            print(f'Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm')