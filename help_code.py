import pandas as pd
import random as rand
import csv

sheet = pd.read_csv('sheet.csv')
length = len(sheet)

print('Wybierz opcje co chcesz zrobić:')
print('1 - wpisywanie haseł do arkusza')
print('2 - nauka haseł')
opt = int(input("Podaj numerek: "))


if opt == 1:
    print("\nJeżeli chcesz zakończyć grę wpisz jako odpowiedź 'q'\n")

    while True:
        term = str(input("Podaj opis: ")).strip()
        ans = str(input("Podaj hasło: ")).strip()

        if ans == 'q':
            break

        if term not in list(sheet['Pytanie']):
            with open('sheet.csv', 'a', newline='', encoding='utf-8') as plik:
                writer = csv.writer(plik)
                writer.writerow([term, ans])

            print("Hasło zostało dodane! \n")

        else:
            print("Hasło znajduje się w słowniku! \n")

if opt == 2:
    print("\nJeżeli chcesz zakończyć grę wpisz jako odpowiedź 'q'\n")

    corr_ans = {}
    wrong_ans = {}

    while True:

        num = rand.randint(0, length-1)
        print(f"Pytanie: {str(sheet['Pytanie'][num].strip())}")
        answer = str(input("Podaj odpowiedź: "))

        if answer == 'q':
            break
        elif answer.strip() == str(sheet['Odpowiedz'][num]).strip():
            print("Poprawna odpowiedz!")

            if str(sheet['Pytanie'][num].strip()) in corr_ans.keys():
                corr_ans[str(sheet['Pytanie'][num].strip())] += 1
            else:
                corr_ans[str(sheet['Pytanie'][num].strip())] = 1

        else:
            print(f"Błąd: Poprawna odpowiedź to: {str(sheet['Odpowiedz'][num]).strip()}")

            if str(sheet['Pytanie'][num].strip()) in wrong_ans.keys():
                wrong_ans[str(sheet['Pytanie'][num].strip())] += 1
            else:
                wrong_ans[str(sheet['Pytanie'][num].strip())] = 1

        print()

    print("Podsumowanie poprawnych pytań (pytanie + ilość poprawnych): ")
    for key, value in corr_ans.items():
        print(str(key), ": ", str(value))

    print("Podsumowanie niepoprawnych pytań (pytanie + ilość niepoprawnych): ")
    for key, value in wrong_ans.items():
        print(str(key), ": ", str(value))