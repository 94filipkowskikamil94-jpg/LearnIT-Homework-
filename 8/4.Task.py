"""Asercja w funkcji: Stwórz funkcję oblicz_srednia(lista_ocen) , która zwraca średnią z
listy. Użyj assert , aby upewnić się, że przekazana lista nie jest pusta"""


lista_ocen = ()

def oblicz_srednia(oceny):

    assert len(oceny) > 0, "Błąd!"

    return sum(oceny) / len(oceny)

srednia = oblicz_srednia(lista_ocen)

print(f"Średnia wynosi: {srednia}")