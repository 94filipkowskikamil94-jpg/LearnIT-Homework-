# Komentowanie kodu: Poniżej znajduje się fragment kodu. Dodaj do niego komentarze
# jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.





def oblicz_pole_prostokata(a, b):
    """Oblicza pole prostokąta na podstawie długości jego dwóch boków."""
    
    # Mnożymy boki a i b, aby uzyskać wynik
    pole = a * b
    
    # Zwracamy obliczoną wartość pole
    return pole


# Definiujemy długości boków prostokąta
bok_a = 10
bok_b = 20

# Wywołujemy funkcję z podanymi bokami i zapisujemy wynik w zmiennej
wynik = oblicz_pole_prostokata(bok_a, bok_b)

# Wyświetlamy sformatowany komunikat na ekranie
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")