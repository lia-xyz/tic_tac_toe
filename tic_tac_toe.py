"""
The Classic Tic-Tac-Toe Game in Python
Author: Natalia Semjonova
Date: 09.03.2025
Description:
A simple command-line Tic-Tac-Toe game written in Python.
"""

# Creates an empty Tic-Tac-Toe board as a dictionary
def create_board():
    return {i: ' ' for i in range(1, 10)}

# Displays the current state of the Tic-Tac-Toe board
def show_board(board):
    print("\n")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("\n")

# Asks the user to choose a position (1-9) to place their mark
def get_user_input(board):
    while True:
        choice = input("Choose the place (1-9): ")
        # Ensure input is a number
        if not choice.isdigit(): 
            print("Invalid input. Please enter a number.")
            continue
        choice = int(choice)
        # Ensure input is within valid range
        if choice not in board: 
            print("Invalid position. Choose a number between 1 and 9.")
            continue
        # Ensure the position is not already taken
        if board[choice] != ' ': 
            print("The place is already taken. Try again.")
            continue
        return choice
    
def is_winner(board, player):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),    # Horizontal wins
        (1, 4, 7), (2, 5, 8), (3, 6, 9),    # Vertical wins
        (1, 5, 9), (3, 5, 7)                # Diagonal wins
    ]
    # Returns True if any of the winning conditions are met
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Runs a single game of Tic-Tac-Toe
def game():
    board = create_board()
    player = 'X'    # X always starts first

    # A full game lasts at most 9 turns
    for turn in range(9):
        show_board(board)
        print(f"It is {player}'s turn.")
        choice = get_user_input(board)      # Get valid user input
        board[choice] = player              # Place player's mark on the board
      
        # Check if the current player has won
        if is_winner(board, player):
            show_board(board)
            print(f"Game Over! Player {player} won!")
            return
        
        # Switch player for the next turn
        player = 'O' if player == 'X' else 'X'

    # If all turns are used and no winner, it's a tie
    show_board(board)
    print("Game over! It is a tie!")

if __name__ == "__main__":
    # Runs the game and asks the user if they want to play again
    while True:
        game()
        if input('Do you want to play again? (y/n): ').lower() != 'y':
            print("Thanks for playing!")
            break
