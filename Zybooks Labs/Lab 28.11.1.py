#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/11
# The words parameter is a list of strings.
def build_dictionary(words):
    word_count = {}  # Initialize an empty dictionary
    for word in words:
        if word in word_count:
            word_count[word] += 1  # Increment the count if the word is already in the dictionary
        else:
            word_count[word] = 1  # Otherwise, add the word to the dictionary with a count of 1
    return word_count

# The following code asks for input, splits the input into a word list, 
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()  # Read input and split it into a list of words
    your_dictionary = build_dictionary(words)  # Build the word frequency dictionary
    sorted_keys = sorted(your_dictionary.keys())  # Get the sorted list of keys
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))  # Print each word and its frequency
