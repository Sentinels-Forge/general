import tkinter as tk


def onClick():
    global clicks
    clicks += 1
    label.config(text=f"Clicks: {clicks}")


root = tk.Tk()
root.title("Tkinter Test App")
root.geometry("500x300")

clicks = 0
label = tk.Label(root, text=f"Clicks: {clicks}")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=onClick)
button.pack()

root.mainloop()
