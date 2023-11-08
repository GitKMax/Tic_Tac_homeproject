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


window = tk.Tk()
window.title("Tic Tac Toe")


buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text="", width=10, height=2, command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)


window.mainloop()