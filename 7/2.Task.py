"""Sortowanie słownika: Masz słownik oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,"Kasia": 4} 
. Użyj funkcji sorted() i funkcji lambda, aby posortować elementy
słownika (klucz, wartość) według ocen (od najwyższej do najniższej)."""

oceny = {"Jan": 4, "Anna": 5, "Biotr": 3,"Kasia": 4}

oceny_sort = sorted(oceny, key = lambda ocena: ocena[1])
oceny_sort_2 = sorted(oceny, key = lambda ocena: ocena[0])
oceny_sort_3 = sorted(oceny, key = lambda ocena: ocena[-1])


print(oceny_sort)
print(oceny_sort_2)
print(oceny_sort_3)