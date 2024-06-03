import random     #provides a suite of functions for generating pseudo-random numbers.
import os.path    #provides a set of functions for working with file paths and directories.
import json       #provides functions for working with JSON data.
random.seed()     # sets the seed for the random number generator.

def draw_board(board):
    '''prints board for tic tac toe'''
    for row in board:
        print("|".join(row))
        

def welcome(board):
    '''displays welcome message'''
    print("Welcome to Tic-Tac-Toe!")
    draw_board(board)

def initialise_board(board):
    '''The function first loops through each row i and column j of the board, and sets the element at that position to a space character " ".'''
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    return board

def get_player_move(board):
    '''this function let user chooose where to put his move within the board we made and stores the move so that it wont be choosed again'''
    valid_input = False
    while not valid_input:
        row = int(input("Please enter the row for your move (1-3): ")) - 1
        col = int(input("Please enter the column for your move (1-3): ")) - 1
        if row in range(3) and col in range(3) and board[row][col] == " ":
            valid_input = True
        else:
            print("Invalid move, please try again.")
    return row, col

def choose_computer_move(board):
    '''this function lets the computer know which moves are available after the user picked the move letting computer choose random move'''
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                available_moves.append((i, j))
    return random.choice(available_moves)

def check_for_win(board, mark):
    # check rows
    for row in board:
        if row[0] == mark and row[1] == mark and row[2] == mark:
            print('you win')
            return True
    # check columns
    for i in range(3):
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            print('you win')
            return True
    # check diagonals
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        print('you win')
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        print('you win')
        return True
    return False

def check_for_draw(board):
    '''if no moves are left and no one won this function calls out draw'''
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def play_game(board):
    '''this function is for iterating the code for infinite loop until one of the condition is match either win or draw'''
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            return 1
        if check_for_draw(board):
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            return -1
        if check_for_draw(board):
            return 0

def menu():
    '''this function let user choose option what to do'''
    choice = input("Please enter 1 to play, 2 to save score, 3 to view leaderboard, or q to quit: ")
    if choice==1:
        play_game(board)
    elif choice==2:
        save_score(score)
    elif choice==3:
        display_leaderboard(leaders)
    elif choice=='q':
        print('Thank you for playing')
    return choice
def load_scores():
    '''this file opens the leaderboard file that already exists in the system'''
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            leaders = json.load(file)
    return leaders

def save_score(score):
    '''this function allows tha user to save the score that you scored playing games in file name leaderboard'''
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    '''This function provides a way to display the leaderboard to the players so they can see their ranking and score in the game.'''
    print("LEADERBOARD")
    for name, score in leaders.items():
        print(f"{name}: {score}")

#Created by: Rabi dhaubanjar
#student id:2329457
