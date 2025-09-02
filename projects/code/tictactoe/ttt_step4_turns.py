import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Tic Tac Toe — Step 4")

current_player = "X"   # start with X

board_frame = tk.Frame(root, padx=10, pady=10)
board_frame.pack()

buttons = []

def on_click(r, c):
    global current_player
    btn = buttons[r][c]

    # If button already clicked, do nothing
    if btn["text"] != "":
        return

    # Set X or O
    btn["text"] = current_player
    btn["state"] = "disabled"

    # Switch turn
    current_player = "O" if current_player == "X" else "X"

# Create a 3x3 grid of buttons
for r in range(3):
    row_btns = []
    for c in range(3):
        btn = tk.Button(board_frame, text="", width=6, height=3, font=("Arial", 16),
                        command=lambda rr=r, cc=c: on_click(rr, cc))
        btn.grid(row=r, column=c, padx=5, pady=5)
        row_btns.append(btn)
    buttons.append(row_btns)

root.mainloop()



def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] != "" and all(buttons[i][j]["text"] == buttons[i][0]["text"] for j in range(3)):
            return buttons[i][0]["text"]
        if buttons[0][1]["text"] != "" and all(buttons[j][i]["text"] == buttons[i][0]["text"] for j in range(3)):
            return buttons[0][i]["text"]
        
    if buttons[0][0]["text"] != "" and all(buttons[i][i]["text"] == buttons[0][0]["text"] for j in range(3)):
            return buttons[0][0]["text"]
    if buttons[0][2]["text"] != "" and all(buttons[i][2-i]["text"] == buttons[0][2]["text"] for j in range(3)):
            return buttons[0][2]["text"]
    return None