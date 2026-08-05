#Praca z f-stringami: Poproś użytkownika o jego imię i rok urodzenia. Oblicz jego
#przybliżony wiek i wyświetl komunikat w formacie: "Cześć, [Imię]! W 2025 roku
#będziesz mieć około [Wiek] lat.

Name = input("What is your name? ")
Born = int(input("What year were you born? "))

print(f"Hi {Name}! In 2025 you will be about {2025-Born} years old. ")