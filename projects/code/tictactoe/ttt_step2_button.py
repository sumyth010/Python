



import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe - Step 2")

# Frame to hold the board 
board_frame = tk.Frame(root,padx=10, pady=10)
board_frame.pack()

# First row of 3 buttons
btn1 = tk.Button(board_frame, text="", width=6, height=3, font=("Arial", 16))
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(board_frame, text="", width=6, height=3, font=("Arial", 16))
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = tk.Button(board_frame, text="", width=6, height=3, font=("Arial", 16))
btn3.grid(row=0, column=2, padx=5, pady=5)



root.mainloop()