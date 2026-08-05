"""Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza
kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania
pliku.
"""
def pokaz_zawartosc_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r") as plik:
            tresc = plik.read()
            print(tresc)
    except FileNotFoundError:
        print("Plik nie istnieje!")
    except PermissionError:
        print("Brak dostępu do pliku!")