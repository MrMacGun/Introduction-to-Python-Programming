# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    
    
    age = int(parts[1]) + 1
    print(f'{name} {age}')
    
    # Get next line
    parts = input().split()
    name = parts[0]