import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Moja pierwsza aplikacja")
root.geometry("300x200")

label = tk.Label(root, text="Podaj swoje imię:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

def say_hello():
    name = entry.get()
    if name:
        messagebox.showinfo("Witaj!", f"Cześć, {name} 👋")
    else:
        messagebox.showwarning("Uwaga", "Wpisz swoje imię!")

button = tk.Button(root, text="Przywitaj się", command=say_hello)
button.pack(pady=10)

root.mainloop()
