import GUI as game_board
import tkinter as tk



def check_winner():
    
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] != "":
            window = tk.Tk()
            label = tk.Label(window, text=f"Player {game_board[row][0]} wins!" )
            label.pack()
            print(f"Player {game_board[row][0]} wins!")
            return

    
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != "":
            print(f"Player {game_board[0][col]} wins!")
            return

    
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "":
        print(f"Player {game_board[0][0]} wins!")
        return
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "":
        print(f"Player {game_board[0][2]} wins!")