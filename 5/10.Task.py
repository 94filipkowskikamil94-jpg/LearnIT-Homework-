# Mini-project: Simple Currency Calculator
# Define exchange rates in a dictionary, e.g., rates = {"USD": 4.0, "EUR": 4.3}
# In a while True loop, ask the user for an amount in PLN and a currency (USD/EUR).
# Use if-elif-else to check the selected currency and calculate the result.
# Format the result to two decimal places using an f-string.
# Ask the user if they want to continue. If they answer "no", use break.

rates = {"USD": 4.0, "EUR": 4.3}

while True:
    amount = float(input("Enter the amount in PLN: "))
    currency = input("Choose currency (USD/EUR): ").upper()

    if currency == "USD":
        print(f"Result: {amount / rates['USD']:.2f} USD")
    elif currency == "EUR":
        print(f"Result: {amount / rates['EUR']:.2f} EUR")
    else:
        print("cChoose USD or EUR.")

    user_choice = input("Do you want to convert amount?: ")
    if user_choice.lower() == "no":
        print("Goodbye!")
        break
