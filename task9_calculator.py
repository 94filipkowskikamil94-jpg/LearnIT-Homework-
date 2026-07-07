number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
sign = input("Enter the operation (-, +, /, *): ")

if sign == "-":
    result = number1 - number2
elif sign == "+":
    result = number1 + number2
elif sign == "/":
    result = number1 / number2
elif sign == "*":
    result = number1 * number2
else:
    print("Invalid operation")

print("The result is:", result)

