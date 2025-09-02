


# gui_app.py 
import tkinter as tk

#create the main Window 
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

# Add a label 
lable = tk.Label(root, text="Enter your name: ")
lable.pack(pady=5)

# Add a text entry field 
entry = tk.Entry(root)
entry.pack(pady=5)


#Function when button is clicked 
def say_hello():
    name = entry.get()
    result_label.config(text=f"Hello, {name}")
    

# Add a button
button = tk.Button(root,text="Say Hello", command=say_hello)
button.pack(pady=10)

# Add a lable for result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)



# Run the app
root.mainloop()