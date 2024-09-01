def format_name(name):
    # Split the input name into parts
    name_parts = name.split()
    
    # Determine the number of parts
    if len(name_parts) == 3:
        # Case with middle name
        first_name = name_parts[0]
        middle_name = name_parts[1]
        last_name = name_parts[2]
        # Format: lastName, firstInitial.middleInitial.
        formatted_name = f"{last_name}, {first_name[0]}.{middle_name[0]}."
    elif len(name_parts) == 2:
        # Case without middle name
        first_name = name_parts[0]
        last_name = name_parts[1]
        # Format: lastName, firstInitial.
        formatted_name = f"{last_name}, {first_name[0]}."
    else:
        # Handle the case where the input format is incorrect
        formatted_name = "Invalid input format."
    
    return formatted_name

# Input from the user
input_name = input("Enter the name: ")

# Get the formatted name and print it
print(format_name(input_name))
