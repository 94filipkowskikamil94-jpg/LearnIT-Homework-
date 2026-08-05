# Kalkulator zniżek: Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
# Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50%
# zniżki. Użyj operatorów or i and .

ticket = 100
discount_price = ticket * 0.5

try:
    age = int(input("Enter your age: "))
    student = input("Are you a student? (yes/no): ").lower()

    if age >= 0 and (age <= 17 or student == "yes"):
        print(f"Ok, you have a 50% discount! Price: {discount_price} PLN")
    elif age >= 18:
        print(f"Regular ticket price: {ticket} PLN")
    else:
        print("Age cannot be negative!")

except ValueError:
    print("You provided incorrect information")