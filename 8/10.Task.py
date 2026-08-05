"""Mini-projekt: Sumator liczb z pliku: Napisz program, który:
a. Pyta użytkownika o nazwę pliku.
b. Otwiera plik i czyta go linia po linii.
c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy po drodze"""


def sumuj_liczby_z_pliku(nazwa):
    suma = 0 
    try:
        with open(nazwa, "r") as plik:
            for linia in plik:
                try:
                    suma += float(linia)
                except ValueError:
                    pass  
    
    except FileNotFoundError:
        print("Nie odnaleziono pliku!")

    finally:
        print(f"Suma: {suma}")


plik_uzytkownika = input("Podaj nazwę pliku: ")
sumuj_liczby_z_pliku(plik_uzytkownika)