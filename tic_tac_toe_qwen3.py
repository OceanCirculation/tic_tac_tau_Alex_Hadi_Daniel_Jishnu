"""
Tic Tac Toe Game
This game was created by Qwen3-Coder AI, an advanced language model designed to assist with programming tasks.

Author: Qwen3-Coder AI
Description: A console-based Tic Tac Toe game using numpy for board representation and game logic.
"""

import numpy as np
import os

class TicTacToe:
    def __init__(self):
        # Create a 3x3 board filled with zeros (0 = empty, 1 = X, -1 = O)
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for X, -1 for O
        self.game_over = False
        self.winner = None
    
    def display_board(self):
        """Display the current board state"""
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        
        print("Tic Tac Toe Game")
        print("Current player: " + ("X" if self.current_player == 1 else "O"))
        print()
        
        # Create a visual representation of the board
        symbols = {0: ' ', 1: 'X', -1: 'O'}
        for i in range(3):
            row = "|"
            for j in range(3):
                row += f" {symbols[self.board[i][j]]} |"
            print(row)
            if i < 2:
                print("-------------")
        print()
    
    def make_move(self, row, col):
        """Make a move at the specified position"""
        if self.game_over:
            return False
            
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
            
        if self.board[row][col] != 0:
            return False
            
        self.board[row][col] = self.current_player
        return True
    
    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if abs(sum(row)) == 3:
                return row[0]
        
        # Check columns
        for col in self.board.T:
            if abs(sum(col)) == 3:
                return col[0]
        
        # Check diagonals
        diag1 = sum(self.board[i][i] for i in range(3))
        diag2 = sum(self.board[i][2-i] for i in range(3))
        
        if abs(diag1) == 3:
            return diag1 // 3
        if abs(diag2) == 3:
            return diag2 // 3
            
        return None
    
    def is_board_full(self):
        """Check if the board is full"""
        return not np.any(self.board == 0)
    
    def switch_player(self):
        """Switch to the other player"""
        self.current_player *= -1
    
    def play(self):
        """Main game loop"""
        print("Welcome to Tic Tac Toe!")
        print("Enter row and column numbers (0-2) to make your move.")
        print("Press Enter after each number.")
        input("Press Enter to start...")
        
        while not self.game_over:
            self.display_board()
            
            # Get player input
            try:
                print(f"Player {self.current_player} turn")
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if not self.make_move(row, col):
                    print("Invalid move! Try again.")
                    input("Press Enter to continue...")
                    continue
                
                # Check for winner
                winner = self.check_winner()
                if winner is not None:
                    self.game_over = True
                    self.winner = winner
                elif self.is_board_full():
                    self.game_over = True
                    self.winner = 0  # Tie
                
                # Switch player if game continues
                if not self.game_over:
                    self.switch_player()
                    
            except ValueError:
                print("Please enter valid numbers!")
                input("Press Enter to continue...")
                continue
        
        # Display final board and result
        self.display_board()
        if self.winner == 0:
            print("It's a tie!")
        else:
            print(f"Player {self.winner} wins!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()