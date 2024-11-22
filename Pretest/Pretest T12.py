#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

file_name = input()  # store name of the file

with open(file_name, 'r') as f:
    word1 = str(f.readline()).strip()  # Read first line of the file, removing whitespace (e.g. \n)
    word2 = str(f.readline()).strip()  # Read second line of the file, removing whitespace (e.g. \n)
    word3 = str(f.readline()).strip()  # Read third line of the file, removing whitespace (e.g. \n)

f = open(file_name, "r")
lines = f.read().splitlines()
lines = ' '.join(lines)
# lines = lines.replace('\n', '')  # You don't need this line, as splitlines() has already done this for you
f.close()  # close the file

print(f"{word1}\n{word2}\n{word3}\n{lines}")
