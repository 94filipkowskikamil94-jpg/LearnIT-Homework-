

# Age Analysis: Write a program that prompts the user for their age. 
# Using if-elif-else statements, display one of the messages: 
# "Infant" (0-1), "Child" (2-12), "Teenager" (13-17), "Adult" (18-64), "Senior" (65+).

try:
    age = int(input("Enter your age:" ))


    if age <= 1:
        print("Infant")
    elif age <= 12:
        print("Child")
    elif age <= 17:
        print("Teenager")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")

except ValueError: 
    print("Please enter a number")