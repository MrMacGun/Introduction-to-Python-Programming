# Main function to determine if the list is a palindrome
def main():
    # Read the length of the list (we don't actually need to use this value in the code)
    n = int(input())
    
    # Read the list of integers
    nums = [int(input()) for _ in range(n)]
    
    # Check if the list is a palindrome by comparing it with its reverse
    if nums == nums[::-1]:
        print("yes")
    else:
        print("no")

# Run the main function
if __name__ == '__main__':
    main()
