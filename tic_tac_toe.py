# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Hi test test test .....
# Hi Britt
# Hi Zina

# Function for ... (displaying the board?)
def blabla():
    pass

# Function for ... (naming the players)
def player_name():
    player1 = input("Write your Playername here: ")
    player2 = input("Write your Playername here: ")
    print("Player 1 is: " + player1)
    print("Player 2 is: " + player2)
    return player1, player2

# Function for... (choosing a player?)
import random

def choose_first_player(p1, p2):
    first = random.choice([p1, p2])
    print(f" {first} starts!")
    return first


# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    p1, p2 = player_name()
    first_player = choose_first_player(p1, p2)
