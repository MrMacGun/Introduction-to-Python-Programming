#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/17


def main():
    
    counts = [0] * 20 
    
    while True:
        num = int(input())
        if num == -1:
            break
        # Increment the count for the number (num - 1) in the list
        if 1 <= num <= 20:
            counts[num - 1] += 1
    
    # Find the mode (the number with the highest count)
    mode = counts.index(max(counts)) + 1
    
    # Output the mode
    print(mode)

# Run the main function
if __name__ == '__main__':
    main()
