# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Hi test test test .....
# Hi Britt
# Hi Zina

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

def create_matrix():
    matrix = []

    for i in range(3):
        matrix.append(["", "", ""])

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" | ".join(row))
        print("---------")

def player_input(player):
    print(f"{player}, it's your turn!")

    row = int(input("Choose a row (1-3): "))
    column = int(input("Choose a column (1-3): "))

    return row, column

def update_matrix(matrix, row, column, symbol):
    matrix[row - 1][column - 1] = symbol
    return matrix

def field_is_free(matrix, row, column):
    return matrix[row - 1][column - 1] == ""

def get_valid_move(matrix, player):
    while True:
        row, column = player_input(player)

        if matrix[row - 1][column - 1] == "":
            return row, column

        print("This field is already occupied. Choose another one.")

# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    p1, p2 = player_name()
    first_player = choose_first_player(p1, p2)

    matrix = create_matrix()
    print_matrix(matrix)

    row, column = get_valid_move(matrix, first_player)
    matrix = update_matrix(matrix, row, column, "X")   

    print_matrix(matrix) 
