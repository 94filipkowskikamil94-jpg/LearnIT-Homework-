#  Średnia ocen: Napisz funkcję oblicz_srednia(*args) , która przyjmuje dowolną liczbę
# ocen (argumentów pozycyjnych) i zwraca ich średnią arytmetyczną. Jeśli nie podano żadnej
# oceny, powinna zwrócić 0

def oblicz_srednia(*args):
    if not args:
        return 0 
    return sum(args)/len(args)

wynik = int(oblicz_srednia(1.03, 2, 3.92, 4, 5))
print(f"Wynik : {wynik}")
