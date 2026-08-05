
#Kalkulator BMI: Napisz program, który zapyta użytkownika o jego wagę w kilogramach i
#wzrost w metrach. Oblicz i wyświetl wskaźnik masy ciała (BMI) według wzoru: BMI = waga
#/ (wzrost * wzrost) 

weight = float(input("How much do you weigh?"))
height = float(input("How tall are you?"))

BMI = weight / (height ** 2)

print(f"Result: {BMI}")