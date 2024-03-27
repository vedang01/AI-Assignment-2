# Code Credit for tic-tac-toe implementation:
# -*- Nuha Alghamdi -*-
# -*- nuhaalghamdi92@gmail.com -*-
# -*- Oct 20 2019 -*-


# Vedang Mishra, 21355044

import random

#to prepare a clean board for the game
def clean_board():
    #an empty board for X and O values
    brd=[" " for x in range(10)]
    return brd

#to check if board is full
def is_board_full(board):
    return board.count(" ")==0

#to insert a letter (X or O) in a specific position
def insert_letter(board,letter,pos):
    board[pos]=letter

#to take computer moves
def computer_move(board,letter):
    computer_letter=letter
    possible_moves=[]
    available_corners=[]
    available_edges=[]
    available_center=[]
    position=-1

    #all possible moves
    for i in range(1,len(board)):
        if board[i] ==" ":
            possible_moves.append(i)

    #if the position can make X or O wins!
    #the computer will choose it to win or ruin a winning of the user
    for let in ["x","o"]:
        for i in possible_moves:
            board_copy=board[:]
            board_copy[i] = let
            if is_winner(board_copy,let):
                position=i


    #if computer cannot win or ruin a winning, then it will choose a random position starting
    #with the corners, the center then the edges
    if position == -1:
        for i in range(len(board)):
            #an empty index on the board
            if board[i]==" ":
                if i in [1,3,7,9]:
                    available_corners.append(i)
                if i == 5:
                    available_center.append(i)
                if i in [2,4,6,8]:
                    available_edges.append(i)
        #check corners first
        if len(available_corners)>0:
            #select a random position in the corners
            position=random.choice(available_corners)
        #then check the availability of the center
        elif len(available_center)>0:
            #select the center as the position
            position=available_center[0]
        #lastly, check the availability of the edges
        elif len(available_edges)>0:
            #select a random position in the edges
            position=random.choice(available_edges)
    #fill the position with the letter
    insert_letter(board, computer_letter, position)


#to draw the board
def draw_board(board):
    board[0]=-1
    #draw first row
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("-"*11)
    #draw second row
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("   |   |   ")
    print("-"*11)
    #draw third row
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("   |   |   ")
    print("-"*11)
    return board

#to check if a specific player is the winner
def is_winner(board,letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
    (board[4] == letter and board[5] == letter and board[6] == letter) or \
    (board[7] == letter and board[8] == letter and board[9] == letter) or \
    (board[1] == letter and board[4] == letter and board[7] == letter) or \
    (board[2] == letter and board[5] == letter and board[8] == letter) or \
    (board[3] == letter and board[6] == letter and board[9] == letter) or \
    (board[1] == letter and board[5] == letter and board[9] == letter) or \
    (board[3] == letter and board[5] == letter and board[7] == letter)

#to play the game
def play_game():

    board=clean_board()
    board=draw_board(board)
    ai_letter = 'o'  # Minimax AI
    auto_letter = 'x'  # Simple strategy AI

    #check if there are empty positions on the board
    while is_board_full(board) == False:
            # Minimax AI move
            print("Minimax AI Move")
            computer_move_minimax(board, ai_letter, alpha_beta_pruning = True)
            board = draw_board(board)
            if is_winner(board, ai_letter):
                print("Minimax AI wins!")
                break

            if is_board_full(board):
                print("Tie Game :)")
                break

            print("Opponent Move")
            # Simple strategy AI move
            computer_move(board, auto_letter)
            board = draw_board(board)
            if is_winner(board, auto_letter):
                print("Opponent wins!")
                break

            print("Both players have made a turn")

    if is_board_full(board) and not is_winner(board, ai_letter) and not is_winner(board, auto_letter):
            print("Tie Game :)")


def computer_move_minimax(board, letter, alpha_beta_pruning):
        best_score = -float('inf')
        best_move = 0
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = letter  # AI's move
                score = minimax(board, 0, False, letter, -float('inf'), float('inf'), alpha_beta_pruning)
                board[i] = " "  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move != 0:
            insert_letter(board, letter, best_move)  # Update the board with the best move


def minimax(board, depth, is_maximizing, letter, alpha, beta, alpha_beta_pruning):
        if letter == 'o':
            opp_letter = 'x'
        else:
            opp_letter = 'o'

        # base case: this is the last state of the game
        if is_winner(board, letter):  # Assuming 'o' is the AI
            # 10 is the maximum depth of the search tree
            return 10-depth
        elif is_winner(board, opp_letter):  # Assuming 'x' is the opponent
            return depth - 10
        elif is_board_full(board):
            return 0

        # if AI's turn to move
        if is_maximizing:
            # initialize best score to negative infinity
            best_score = -float('inf')

            # iterate through all the empty positions that can be reached in a single move
            for i in range(1, 10):
                if board[i] == " ":
                    board[i] = letter # AI's move
                    # recursive call to minimax, switching players
                    score = minimax(board, depth + 1, False, letter, alpha, beta, alpha_beta_pruning)
                    board[i] = " "  # Undo move
                    # choose best score
                    best_score = max(score, best_score)
                    if alpha_beta_pruning:
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(1, 10):
                if board[i] == " ":
                    board[i] = opp_letter
                    score = minimax(board, depth + 1, True, letter, alpha, beta, alpha_beta_pruning)
                    board[i] = " "  # Undo move
                    # opponent wants to minimize score
                    best_score = min(score, best_score)
                    if alpha_beta_pruning:
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score


#Start the game
play_game()