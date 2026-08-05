#  Kalkulator: Napisz funkcję kalkulator(a, b, operacja) , która przyjmuje dwie liczby i
# string z operacją ( "+" , "-" , "*" lub / "). Funkcja powinna zwracać wynik
# odpowiedniego działania.


def kalkulator(a, b, operacja):
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

