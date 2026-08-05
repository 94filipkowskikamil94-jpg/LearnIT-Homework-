"""Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz  (gdy nie
ma uprawnień do odczytu)."""


def pokaz_zawartosc_pliku(nazwa_pliku):
    plik = None
    try:
        plik = open(nazwa_pliku, "r")
        tekst = plik.read()
        print(tekst)
    except FileNotFoundError:
        print("Plik nie isntnieje")
    except PermissionError:
        print("Brak dostepu do plików")

    finally:
        if plik:
            plik.close()
