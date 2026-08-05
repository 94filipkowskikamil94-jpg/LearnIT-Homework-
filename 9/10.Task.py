"""Mini-projekt: Lista zadań: Stwórz prostą aplikację do zarządzania listą zadań. Program
powinien:
Przy starcie próbować wczytać zadania z pliku zadania.json .
Pozwalać użytkownikowi dodać nowe zadanie.
Pozwalać wyświetlić wszystkie zadania.
Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku"""

import json

lista_zadan = []


try:
    with open("zadania.json", "r", encoding="utf8") as plik:
        lista_zadan = json.load(plik)
except FileNotFoundError:
    print("Błąd")

while True:
    
    wybor = input("Wciśnij [1] gdy chcesz zobaczyć zadania\nWciśnij [2] aby wpisać nowe zadanie\nWciśnij [3] aby zamknąć\nWybierz opcję: ")
    if wybor == "1":
        print(lista_zadan)
    elif wybor == "2":
        nowe_zadanie = input("Napisz nowe zadanie:\n")
        lista_zadan.append(nowe_zadanie)
    elif wybor == "3":
        print("Wyłaczam .....")
        with open("zadania.json", "w", encoding="utf8") as plik:
            json.dump(lista_zadan, plik)
        break
    else:
        print("Błąd, napisz jeszcze raz")


