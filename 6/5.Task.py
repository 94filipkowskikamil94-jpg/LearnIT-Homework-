# Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. Dodaj do niej pełne
# adnotacje typów dla wszystkich parametrów i wartości zwracanej. Napisz również
# kompletny docstring opisujący jej działanie

def kalkulator(a, b, operacja):

    """Wykonuje podstawową operację matematyczną na dwóch liczbach.

    Parametry:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.
        operacja (str): Znak działania ('+', '-', '*', '/').

    Zwraca:
        float | str: Wynik działania lub informacja o błędnym operatorze."""

    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b
    else:
        return "Invalid operator!"


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
znak = input("Enter operator (+, -, *, /): ")

wynik = kalkulator(num1, num2, znak)
print(f"Result: {wynik}")
