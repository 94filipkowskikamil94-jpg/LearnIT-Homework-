'''Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) , która rzuca własnym,
zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż
18. Napisz kod, który wywołuje tę funkcję i obsługuje ten wyjątek'''

class WiekNiepoprawnyError(Exception):
    pass

wiek = int(input("Podaj wiek: "))
if wiek <18:
    raise WiekNiepoprawnyError("Za mały wiek")

