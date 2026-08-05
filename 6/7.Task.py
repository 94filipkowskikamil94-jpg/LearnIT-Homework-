# Zwracanie wielu wartości: Stwórz funkcję analiza_listy(lista: list[int]) , która
# przyjmuje listę liczb i zwraca krotkę zawierającą trzy wartości: minimum, maksimum i sumę
# elementów z listy.

def analiza_listy(lista: list[int])-> tuple[int, int, int]:
      return max(lista), min(lista), sum(lista)

liczby = [51, 54, 17, 12, 942]

największa, najmniejsza, suma = analiza_listy(liczby)
print(f"Min: {najmniejsza}, Max: {największa}, Suma: {suma}")