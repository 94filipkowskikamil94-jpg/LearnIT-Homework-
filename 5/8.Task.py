# 8. Wyszukiwarka w liście: Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr",
# "Kasia"] . Poproś użytkownika o podanie imienia do wyszukania. Użyj pętli for z
# instrukcją break oraz blokiem else , aby:
# Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę.
# Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia na
# liście"

name = ["Anna", "Jan", "Piotr"]
new_name = input("Enter a name: ")

for i in name:
    
    if i == new_name:
        print("Good job !") 
        break
    else:
        print("Once again")

    
