"""Przerzucanie wyjątku: Napisz funkcję przetworz_dane(dane) , która w bloku
try...except łapie KeyError (np. przy próbie dostępu do nieistniejącego klucza w
słowniku), loguje go, a następnie rzuca ( raise ) nowy, własny wyjątek
BladPrzetwarzaniaDanychError z informacją, którego klucza brakowało"""


class BladPrzetwarzaniaDanychError(Exception):
    pass

def przetworz_dane(dane):
    try:
        return dane["wiek"] 
    except KeyError as e:
        print("Nie znaleziono podanego klucza")
        
        raise BladPrzetwarzaniaDanychError(f"Brakujący klucz: {e}")

testowy_slownik = {"imie": "Ania"}
przetworz_dane(testowy_slownik)