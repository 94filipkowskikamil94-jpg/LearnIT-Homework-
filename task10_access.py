
height = int(input("Enter your height in centimeters: "))
adults = input("Are you with adults? (yes/no): ")

if height < 120:
        print("You are too short")
elif height > 160:
        print("Its okey")
elif height >= 120 and height <= 160 and adults == "no":
        print(" You are small")
elif height >= 120 and height <= 160 and adults == "yes":
        print("You can ride with an adult.")
else:
        print("Invalid input.")
