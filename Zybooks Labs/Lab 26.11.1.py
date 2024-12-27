https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/11
import random

# Function to simulate a coin flip
def coin_flip():
    flip = random.randint(0, 1)  # Generates 0 or 1
    if flip == 1:
        return "Heads"
    else:
        return "Tails"

# Main program
if __name__ == '__main__':
    random.seed(5)  # Unique seed for consistent random results
    number_of_flips = int(input())  # Read the number of flips
    
    # Perform the coin flips and output the result of each flip
    for _ in range(number_of_flips):
        print(coin_flip())