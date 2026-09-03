import numpy as np

# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def get_player_name():
    
    player_1_name= input("(Please choose your name between X & O)" )
    permitted_name = ["X","O"] 

    if player_1_name in permitted_name :
        if player_1_name == permitted_name[0]:
           player_2_name = permitted_name[1] 
        else:
           player_2_name = permitted_name[0]  

        #print("Player_1 Name is: ",player_1_name,"Player_2 Name is: ", player_2_name)
        return player_1_name, player_2_name 
    else:
        print("Wrong!! Only X & O are accepted")
        player_1_name, player_2_name = "0","0"
        return player_1_name, player_2_name

# Function for... (choosing a player?)
def check_win_con(board):
    winning_con = False 
    board_check=board.copy()
    board_check[board_check == "X"] = "0"
    board_check[board_check == "O"] = "1"
    board_check[board_check == ""] = "8"
    board_check_int = board_check.astype(int)
    sum_row = np.sum(board_check_int,axis=0)
    sum_column = np.sum(board_check_int,axis=1)
    #print("Summation of row is",sum_row)

    if np.any(sum_row == 0) or np.any(sum_row == 3) or np.any(sum_column == 0) or np.any(sum_column == 3):
        winning_con = True 
  
    return winning_con
    #board =np.int(board)
    #print("testing function:", board_check_int)

def main():
    player_1, player_2 = get_player_name()
    print("Player_1 Name is: ",player_1,"Player_2 Name is: ", player_2)
    board = np.zeros((3,3),dtype=str)
    print(board)

    # Asking for players input
    active_player = player_1
    inactive_player = player_2 
    i_loop = 1 
    while i_loop <= 9 :
        sel_row=int(input(f"{active_player} please add you desire element (row)"))
        sel_column=int(input(f"{active_player} please add you desire element (column)"))
        print(board[sel_row-1][sel_column-1])

        if board[sel_row-1][sel_column-1] == "" :
            board[sel_row-1][sel_column-1] = active_player
        else:
            print("Already taken")
            continue

        print(board) 
        Check_win = check_win_con(board) 
        print(Check_win) 
        if Check_win:
            print(f"Game is over.{active_player} WON the game. Congratulations !!! ")
        else:
            print("Game is NOT over")
        
        active_player, inactive_player = inactive_player, active_player
        i_loop += 1
        
# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round 
    print("Welcome to a new round of Tic-Tac-Toe!")
    main()
 