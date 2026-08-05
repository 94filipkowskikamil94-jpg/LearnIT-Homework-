"""Wyszukiwarka logów: Wyobraź sobie, że masz duży plik log.txt . Napisz program, który
pyta użytkownika o szukane słowo (np. "ERROR") i zapisuje wszystkie linie zawierające to
słowo do nowego pliku wyniki_wyszukiwania.txt"""

slowo = input("Podaj słowo: ")
znaleziono = False 

with open("log.txt", "r", encoding="utf-8") as plik, open("wyniki_wyszukiwania.txt", "w", encoding="utf-8") as wy_plik:
    for linia in plik:
        if slowo in linia:
            wy_plik.write(linia)
            znaleziono = True 
            
if znaleziono:
    print(f"Sukces! {slowo}")
else:
    print(f"Porażka! {slowo}")