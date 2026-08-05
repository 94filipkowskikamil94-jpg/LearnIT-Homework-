# Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego
# treścią) był zapisywany do pliku log.txt , a program kontynuował działanie. Użyj bloku
# finally , aby upewnić się, że plik z logami jest zawsze zamykany

def Oblicz(a: float, b: float, operacja: str) -> float:
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b

plik_log = open("log.txt", "a", encoding="utf-8")

try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        oper = input("Podaj operację ( + , - , * , / ): ")

        obliczenia = Oblicz(num1, num2, oper)

except ValueError as e:
    print("BŁĄD: Podana wartość nie jest liczbą!")
    plik_log.write(f"Błąd {e}")
except ZeroDivisionError as e:
    print("BŁĄD: Nie można dzielić przez zero!")
    plik_log.write(f"Błąd 0 {e}")   
else:
    print(f"Wynik: {obliczenia}")
finally:
    plik_log.close()
    print("Zakończono operację (plik logów zamknięty).")
