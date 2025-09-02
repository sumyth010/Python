



import tkinter as tk


root = tk.Tk()
root.title("Tic Tac Toe -  Step 3")

board_frame = tk.Frame(root, padx=10, pady=10)
board_frame.pack()



buttons = []
for r in range (3):
    row_btns = []
    for c in range(3):
        btn = tk.Button(board_frame, text="", width=6, height=3, font=("Arial", 16))
        btn.grid(row=r, column=c, padx=5, pady=5)
        row_btns.append(btn)
    buttons.append(row_btns)
    
root.mainloop()