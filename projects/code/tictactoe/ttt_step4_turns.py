import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"   # start with X
buttons = []

def check_winner():
    # Check rows and columns
    for i in range(3):
        # Row
        if buttons[i][0]["text"] != "" and all(buttons[i][j]["text"] == buttons[i][0]["text"] for j in range(3)):
            return buttons[i][0]["text"]
        # Column
        if buttons[0][i]["text"] != "" and all(buttons[j][i]["text"] == buttons[0][i]["text"] for j in range(3)):
            return buttons[0][i]["text"]

    # Diagonals
    if buttons[0][0]["text"] != "" and all(buttons[i][i]["text"] == buttons[0][0]["text"] for i in range(3)):
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] != "" and all(buttons[i][2-i]["text"] == buttons[0][2]["text"] for i in range(3)):
        return buttons[0][2]["text"]

    return None

def on_click(r, c):
    global current_player
    btn = buttons[r][c]

    if btn["text"] != "":
        return

    btn["text"] = current_player
    btn["state"] = "disabled"

    # Check winner
    winner = check_winner()
    if winner:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        for row in buttons:
            for b in row:
                b["state"] = "disabled"
        return
    elif all(button["text"] != "" for row in buttons for button in row):
        messagebox.showinfo("Game Over", "It's a draw!")
        return

    # Switch turn
    current_player = "O" if current_player == "X" else "X"

# Create a 3x3 grid of buttons
board_frame = tk.Frame(root, padx=10, pady=10)
board_frame.pack()

for r in range(3):
    row_btns = []
    for c in range(3):
        btn = tk.Button(board_frame, text="", width=6, height=3, font=("Arial", 16),
                        command=lambda rr=r, cc=c: on_click(rr, cc))
        btn.grid(row=r, column=c, padx=5, pady=5)
        row_btns.append(btn)
    buttons.append(row_btns)

root.mainloop()
