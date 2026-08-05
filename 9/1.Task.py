"""Dziennik użytkownika: Napisz program, który w pętli prosi użytkownika o wpisanie jednej
linii tekstu. Każda wpisana linia powinna być dopisywana (tryb 'a' ) do pliku
dziennik.txt . Program kończy działanie, gdy użytkownik wpisze "koniec"""

while True:
    tekst = input("Napisz tekst: ")
    
    if tekst == "koniec":
        print("Koniec programu!")
        break
    
    with open("dziennik.txt", "a") as plik:
        plik.write(tekst + "\n")

    with open("dziennik.txt", "r") as plik:
        zawartosc = plik.read()
        print("--- ZAWARTOŚĆ DZIENNIKA ---")
        print(zawartosc)