import tkinter as tk


def calculate():
    try:
        result = eval(entry.get())
        output_label.config(text=f"Result: {result}")
    except Exception as e:
        output_label.config(text=f"Error: {e}")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x150")

input_label = tk.Label(root, text="Enter Expression:")
input_label.pack()

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack()

output_label = tk.Label(root, text="Result: ")
output_label.pack(pady=10)

root.mainloop()
