"""Znajdowanie liczb pierwszych: Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać
tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , która
sprawdza, czy liczba jest pierwsza)"""


listy = range(1, 31)

def czy_pierwsza(n) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

listy = range(1, 31)

liczby_pierwsze = list(filter(czy_pierwsza, listy))

print(liczby_pierwsze)
