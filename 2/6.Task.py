id_car = input("Do you have driver's license (yes/no):")
age = int(input("Enter your age: "))

if age >= 18 and id_car.lower() == "yes":
    print("You can drive.")
else:
    print("You are not old enough to drive.")

print(id_car)