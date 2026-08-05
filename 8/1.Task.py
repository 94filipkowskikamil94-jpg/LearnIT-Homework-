"""Bezpieczny kalkulator: Napisz program, który w pętli prosi użytkownika o podanie dwóch
liczb i operacji ( + , - , * , / ). Zaimplementuj pełną obsługę błędów ValueError (gdy
dane nie są liczbami) i ZeroDivisionError . Dodaj blok else do wyświetlania wyniku i
finally z komunikatem "Kolejna operacja..."""

def Oblicz(a: float, b: float, operacja: str) -> float:
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b

try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        oper = input("Podaj operację ( + , - , * , / ): ")

        obliczenia = Oblicz(num1, num2, oper)

except ValueError:
        print("BŁĄD: Podana wartość nie jest liczbą!")
except ZeroDivisionError:
        print("BŁĄD: Nie można dzielić przez zero!")
else:
        print(f"Wynik: {obliczenia}")
finally:
        print("Kolejna operacja...")


