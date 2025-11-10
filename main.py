import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random

def add_key():
    window = tk.Toplevel(root)
    window.title("Dodawanie klucza")
    window.geometry("500x750")

    L1 = tk.Label(window, text='Wprowadź hasło i klucz').pack()

    E1 = tk.Entry(window, bd=5)
    E1.pack()
    E2 = tk.Entry(window, bd=5)
    E2.pack()


    def take_data():
        pyt = E1.get().strip()
        odp = E2.get().strip()

        duplikat = ((sheet['Pytanie'] == pyt) & (sheet['Odpowiedz'] == odp)).any()

        if pyt == "" or odp == "":
            messagebox.showwarning("Błąd", "Wpisz oba pola!")
            return

        if duplikat:
            messagebox.showinfo("Informacja", "Ten wpis już istnieje w arkuszu.")
        else:
            sheet.loc[len(sheet)] = [pyt, odp]
            sheet.to_csv('sheet.csv', index=False)
            messagebox.showinfo("Sukces", "Dodano nowe hasło do arkusza!")
            window.destroy()

    B1 = tk.Button(window, text='Zatwierdź', command=take_data).pack(pady=10)

def learn():
    window = tk.Toplevel(root)
    window.title("Nauka słówek")
    window.geometry("500x750")

    L1 = tk.Label(window, text="Wprowadź odpowiedź na podane pytanie: ").pack()
    rand_index = random.randint(a=0, b=len(sheet))
    pyt = sheet.iloc[rand_index]['Pytanie']
    odp = sheet.iloc[rand_index]['Odpowiedz']
    L2 = tk.Label(window, text=f"{pyt}").pack()
    E1 = tk.Entry(window, bd=5)
    E1.pack()

    def take_data():
        odp_user = " ".join(E1.get().split())
        if odp_user == "":
            messagebox.showwarning("Błąd", "Wpisz odpowiedź!")
            return
        if odp_user != odp:
            messagebox.showinfo("Informacja", "Błędne hasło!")
        else:
            messagebox.showinfo("Informacja", "Poprawne hasło!")

    B1 = tk.Button(window, text='Zatwierdź', command=take_data).pack(pady=10)

    window.mainloop()

def select_sheet():
    window = tk.Toplevel(root)
    window.title("Sheet z danymi")
    window.geometry("1000x750")


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

sheet = pd.read_csv('sheet.csv')

B1 = tk.Button(root, text='Dodaj hasło do arkusza', command=add_key)
B1.place(x=50, y=50)
B2 = tk.Button(root, text='Ucz się haseł z arkusza', command=learn)
B2.place(x=50, y=100)
B3 = tk.Button(root, text='Wyświetl arkusz', command=select_sheet)
B3.place(x=50, y=150)

root.mainloop()
