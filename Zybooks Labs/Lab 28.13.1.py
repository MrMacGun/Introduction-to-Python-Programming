#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/13
roster = {}
for i in range(1, 6):
    jpy = int(input(f"Enter player {i}'s jersey number:\n"))
    jr = int(input(f"Enter player {i}'s rating:\n"))
    print("")
    roster[jpy] = jr

def input_player_data():
    roster = {}
    for i in range(5):
        jersey_number = int(input(f"Enter player {i + 1}'s jersey number: "))
        rating = int(input(f"Enter player {i + 1}'s rating: "))
        roster[jersey_number] = rating
    return roster

def output_roster(roster):
    print("\nROSTER")
    for jersey_number in sorted(roster.keys()):
        print(f"Jersey number: {jersey_number}, Rating: {roster[jersey_number]}")

def display_menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

def add_player(roster):
    jersey_number = int(input("Enter a new player's jersey number: "))
    rating = int(input("Enter the player's rating: "))
    roster[jersey_number] = rating

def remove_player(roster):
    jersey_number = int(input("Enter a jersey number: "))
    if jersey_number in roster:
        del roster[jersey_number]

def update_player_rating(roster):
    jersey_number = int(input("Enter a jersey number: "))
    if jersey_number in roster:
        rating = int(input("Enter a new rating for player: "))
        roster[jersey_number] = rating

def output_players_above_rating(roster):
    rating_threshold = int(input("Enter a rating: "))
    print(f"\nABOVE {rating_threshold}")
    for jersey_number, rating in sorted(roster.items()):
        if rating > rating_threshold:
            print(f"Jersey number: {jersey_number}, Rating: {rating}")

def main():
    roster = input_player_data()
    while True:
        display_menu()
        option = input("Choose an option: ")
        if option == 'q':
            break
        elif option == 'o':
            output_roster(roster)
        elif option == 'a':
            add_player(roster)
        elif option == 'd':
            remove_player(roster)
        elif option == 'u':
            update_player_rating(roster)
        elif option == 'r':
            output_players_above_rating(roster)

# Run the program
main()
