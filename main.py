import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random

def add_key():
    window = tk.Toplevel(root)
    window.title("Dodawanie klucza")
    window.geometry("500x750")

    tk.Label(window, text='Wprowadź hasło i klucz').pack(pady=10)

    E1 = tk.Entry(window, bd=5)
    E1.pack(pady=5)

    E2 = tk.Entry(window, bd=5)
    E2.pack(pady=5)

    label_info = tk.Label(window, text="", font=("Arial", 12))
    label_info.pack(pady=10)

    def take_data():
        pyt = E1.get().strip()
        odp = E2.get().strip()

        if pyt == "" or odp == "":
            label_info.config(text="❌ Wpisz oba pola")
            return

        duplikat = ((sheet['Pytanie'] == pyt) & (sheet['Odpowiedz'] == odp)).any()

        if duplikat:
            label_info.config(text="⚠️ Ten wpis już istnieje")
        else:
            sheet.loc[len(sheet)] = [pyt, odp]
            sheet.to_csv('sheet.csv', index=False)
            label_info.config(text="✅ Zapisano poprawnie")

            # czyszczenie pól
            E1.delete(0, tk.END)
            E2.delete(0, tk.END)
            E1.focus()

    tk.Button(window, text='Zatwierdź', command=take_data).pack(pady=10)


def learn():
    window = tk.Toplevel(root)
    window.title("Nauka słówek")
    window.geometry("500x750")

    label_pyt = tk.Label(window, font=("Arial", 16))
    label_pyt.pack(pady=20)

    E1 = tk.Entry(window, bd=5)
    E1.pack()

    label_info = tk.Label(window, text="", font=("Arial", 12))
    label_info.pack(pady=10)

    def new_word():
        nonlocal pyt, odp
        rand_index = random.randint(0, len(sheet) - 1)
        pyt = sheet.iloc[rand_index]['Pytanie']
        odp = sheet.iloc[rand_index]['Odpowiedz']

        label_pyt.config(text=pyt)
        E1.delete(0, tk.END)
        label_info.config(text="")
        E1.focus()

    def take_data():
        odp_user = " ".join(E1.get().split())
        if odp_user == "":
            messagebox.showwarning("Błąd", "Wpisz odpowiedź!")
            return

        if odp_user == odp:
            label_info.config(text="✅ Poprawna odpowiedź")
        else:
            label_info.config(text=f"❌ Błędna odpowiedź\nPoprawna: {odp}")

        # po 5 sekundach nowe hasło
        window.after(2000, new_word)

    tk.Button(window, text='Zatwierdź', command=take_data).pack(pady=10)

    # pierwsze hasło
    pyt = odp = ""
    new_word()

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
