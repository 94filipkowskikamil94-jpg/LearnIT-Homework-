#  Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . Napisz
# funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego
# global . Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. Wyświetl wartość
# zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.

POZIOM_DOSTEPU = "user" 

def zmiana():
    POZIOM_DOSTEPU = "admin"
    print(f"{POZIOM_DOSTEPU}")
    
zmiana()
print(f"{POZIOM_DOSTEPU}")