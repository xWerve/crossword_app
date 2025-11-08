import tkinter as tk
from tkinter import ttk
import pandas as pd

def add_key():
    window = tk.Toplevel(root)
    window.title("Dodawanie klucza")
    window.geometry("500x750")

    L1 = tk.Label(window, text='Wprowadź hasło i klucz').pack()

    E1 = tk.Entry(window, bd=5)
    E1.pack()
    E2 = tk.Entry(window, bd=19)
    E2.pack()

    window.mainloop()
def learn():
    window = tk.Toplevel(root)
    window.title("Nauka słówek")
    window.geometry("500x750")
def select_sheet():
    window = tk.Toplevel(root)
    window.title("Sheet z danymi")
    window.geometry("500x750")


    sheet = pd.read_csv('sheet.csv')

    table = ttk.Treeview(window, columns=("kol1", "kol2"))
    table.heading("kol1", text="Pytanie")
    table.heading("kol2", text="Odpowiedź")

    for index, row in sheet.iterrows():
        table.insert("", tk.END, values=(row.iloc[0], row.iloc[1]))
    table.pack(fill="both", expand=True, padx=10, pady=10)

    window.mainloop()

root = tk.Tk()

root.title("Crossward App")
root.geometry("1500x750")

B1 = tk.Button(root, text='Dodaj hasło do arkusza', command=add_key)
B1.place(x=50, y=50)
B2 = tk.Button(root, text='Ucz się haseł z arkusza', command=learn)
B2.place(x=50, y=100)
B3 = tk.Button(root, text='Wyświetl arkusz', command=select_sheet)
B3.place(x=50, y=150)

root.mainloop()
