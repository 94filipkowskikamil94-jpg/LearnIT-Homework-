"""Filtrowanie słów: Mając listę słów slowa = ["jabłko", "banan", "kiwi", "gruszka",
"truskawka"] , użyj list comprehension, aby stworzyć nową listę zawierającą tylko te
słowa, które mają więcej niż 5 liter"""
# liczby_slownik = {x: x ** 2 for x in range(1, 5)

slowa = ["jabłko", "banan", "kiwi", "gruszka", "truskawka"]

slowa_v2 = [slowo for slowo in slowa if len(slowo) > 5]

print(slowa_v2)