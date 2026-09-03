# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

import numpy as np

def check_winner(board):
    won = False 
    # I am way too lazy to write the checks by hand so I will use numpy to check if any row, column or diagonal has all the same values (1 or 2)
    # The text completion is scary...
    if (np.any(np.all(board == 1, axis=0)) or np.any(np.all(board == 1, axis=1)) or np.all(np.diag(board) == 1) or np.all(np.diag(np.fliplr(board)) == 1)):
        won = True
    return won

def display_board(board):
    print(board.reshape(3,3))
    pass

"""
Get the move from the player. On a 3x3 field the player can choose a number from 1 to 9. The function should return the number that the player has chosen.
todo: error handling - what if the number is > 9 or a string?
"""
def get_player_move(board, player):
    print(f"Player {player}, please enter your move (1-9): ")
    position = int(input())
    if ((board.reshape(9,1)[position-1] is 0)):
        print("This position is already taken. Please choose another one.")
        return get_player_move(board, player)
    else:
        board.reshape(9,1)[position-1] = player
    return position

def main():
    print("Welcome to a new round of Tic-Tac-Toe!")
    print ("Player 1 is X and Player 2 is O. The board positions are numbered as follows:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

    board = np.zeros((3, 3), dtype=int)
    while True:
    
        display_board(board)    
        get_player_move(board, 1)
        if (check_winner(board)):
            print("Player 1 wins!")
            break

        if (np.all(board != 0)):
            print("It's a draw!")
            break
        display_board(board)    
        get_player_move(board, 2)
        check_winner(board)
        if (check_winner(board)):
            print("Player 2 wins!")
            break
        if (np.all(board != 0)):
                    print("It's a draw!")
                    break
# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    main()
    
