#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/16

# Main function to shift elements to the right
def main():
    # Read the number of integers in the list
    n = int(input())
    
    # Read the list of integers
    nums = [int(input()) for _ in range(n)]
    
    # Perform the right shift: move the last element to the first
    if len(nums) > 1:
        last_element = nums[-1]
        # Shift all elements one position to the right
        nums = [last_element] + nums[:-1]
    
    # Output the modified list, with each element followed by a space
    for num in nums:
        print(num, end=" ")
    print()  # To print a newline after the output

# Run the main function
if __name__ == '__main__':
    main()

