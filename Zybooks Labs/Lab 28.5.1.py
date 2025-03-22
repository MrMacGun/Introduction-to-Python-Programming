#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/5
def reverse_list(letters):
    # Initialize an empty list to store the reversed order
    reversed_list = []
    
    # Loop through the input list in reverse order
    for i in range(len(letters)-1, -1, -1):
        reversed_list.append(letters[i])
    
    return reversed_list

if __name__ == '__main__':
    ch = ['a', 'b', 'c']
    print(reverse_list(ch))  # Should print ['c', 'b', 'a']
