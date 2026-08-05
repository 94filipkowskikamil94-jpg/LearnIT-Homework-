# Gra "Zgadnij liczbę":
# Program "myśli" o liczbie (np. sekret = 42 ).
# Użyj pętli while True , aby w nieskończoność prosić użytkownika o podanie liczby.
# Wewnątrz pętli, sprawdź, czy podana liczba jest równa sekretnej. Jeśli tak, wyświetl
# gratulacje i użyj break , aby zakończyć grę. Jeśli nie, poinformuj, że to zła liczba
import random

secret = random.randint(1,10)

while secret:
    num = int(input("Enter your number: "))
    if num == secret:
        print("super!")
        break
    else:
        print("Once again")



