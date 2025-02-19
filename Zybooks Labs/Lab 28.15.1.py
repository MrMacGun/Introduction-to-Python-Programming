

# Main function to swap the first and last elements
def main():
    # Read the list of integers from input
    nums = list(map(int, input().split()))
    
    # Swap the first and last elements if the list has more than one element
    if len(nums) > 1:
        nums[0], nums[-1] = nums[-1], nums[0]
    
    # Output the modified list, with each element followed by a space
    for num in nums:
        print(num, end=" ")
    print()  # To print a newline after the output

# Run the main function
if __name__ == '__main__':
    main()
