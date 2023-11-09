import tkinter as tk

game_board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def button_click(row, col):
    global current_player

    if game_board[row][col] == "":
        game_board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        check_winner()

def check_winner():
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] != "":
            label.config(text=f"Player {game_board[row][0]} wins!")
            return

    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != "":
            label.config(text=f"Player {game_board[0][col]} wins!")
            return

    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "":
        label.config(text=f"Player {game_board[0][0]} wins!")
        return
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "":
        label.config(text=f"Player {game_board[0][2]} wins!")

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")

buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text="", width=18, height=7, command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

label = tk.Label(window, text="", font=('Arial', 18), width=20, height=2)
label.grid(row=4, column=0, columnspan=3)

window.mainloop()
