# Bramki logiczne: Napisz program, który poprosi o dwie wartości logiczne ( True lub
# False ). Niech użytkownik wprowadza 1 dla True i 0 dla False . Program powinien
# wyświetlić wyniki operacji AND oraz OR dla tych dwóch wartości

num = int(input("Enter  1 or 0:  "))
num1 = int(input("Enter 1 or 0:  "))

val = bool(num)
val1 = bool(num1)

result_AND = val and val1
result_OR = val or val1

print(f"{result_AND}")
print(f"{result_OR}")