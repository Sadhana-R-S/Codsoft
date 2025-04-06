import tkinter as tk
def on_click(button_value):
    entry.insert(tk.END, button_value)  
def clear():
    entry.delete(0, tk.END) 
def calculate():
    try:
        result = eval(entry.get())  
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.config(bg="blue")
entry = tk.Entry(root, bg="pink",fg="blue",font=("Monaco", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
frame = tk.Frame(root)
frame.config(bg="purple")
frame.pack()
row, col = 0, 0
for button in buttons:
    action = lambda b=button: on_click(b) if b != "=" else calculate()
    tk.Button(frame, bg="pink",fg="purple",text=button, width=5, height=2, font=("Monaco", 14,"bold"),
              command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
tk.Button(root, text="Clear", width=20, height=2, font=("Arial", 14), command=clear).pack(pady=5)
root.mainloop()
