#pig game
import random

def roll_dice():
    return random.randint(1, 10)
      
while True:
    print("\nWelcome to the Pig Game!\n")
    players = int(input("Enter the number of players: "))
    if players < 2:
        print("Please enter at least 2 players.")
        continue
    else:
        break

max_score = 20

while True:
    total_scores = [0] * players
    game_won = False

    while not game_won:
        for player_index in range(players):

            if game_won:
                break

            print(f"\nPlayer {player_index + 1}'s turn. \nCurrent score: {total_scores[player_index]}")

            turn_score = 0

            while True:
                roll = roll_dice()
                print(f"\nPlayer {player_index + 1} rolled a {roll}.")

                if roll == 1:
                    print("Oh no! You rolled a 1. Your turn is over and you lose all points for this turn.")
                    turn_score = 0
                    break
                else:
                    turn_score += roll
                    print(f"Your turn score is now {turn_score}.")

                if turn_score >= max_score:
                    print(f"\nCongratulations! Player {player_index + 1} wins with a score of {total_scores[player_index] + turn_score}!\n")
                    game_won = True
                    break
                choice = input("\nDo you want to roll again or hold? (y/n): ").lower()
                if choice != 'y':
                    total_scores[player_index] += turn_score
                    print(f"Your total score is now {total_scores[player_index]}.")
                    break

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break

 
