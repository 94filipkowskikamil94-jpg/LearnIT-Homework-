"""Licznik słów: Stwórz program, który pyta o nazwę pliku, odczytuje go, a następnie zlicza i
wyświetla całkowitą liczbę słów w tym pliku. Obsłuż błąd FileNotFoundError , jeśli plik nie
istnieje"""

while True:
    try:
    
        nazwa_pliku = input("Podaj nazwę pliku: ")
        
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            tekst = plik.read()
            lista_slow = tekst.split()
            ilosc = len(lista_slow)
            print(f"W pliku jest {ilosc} .")
            break 

    except FileNotFoundError:
       
        print("Plik nie istnieje. \n")

