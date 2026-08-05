"""Mini-projekt: Przetwarzanie danych: Masz listę słowników reprezentujących
użytkowników:
Napisz jednolinijkowy kod (używając kombinacji filter , map lub list comprehension),
który zwróci listę imion aktywnych użytkowników, którzy mają 18 lat lub więcej, pisanych
wielkimi literami."""

uzytkownicy = [
{"imie": "Jan", "wiek": 30, "aktywny": True},
{"imie": "Anna", "wiek": 17, "aktywny": False},
{"imie": "Piotr", "wiek": 25, "aktywny": True}]

# uzytkownicy2 = list(
#     map(
#         lambda x: x["imie"].upper(), filter(lambda x: x["wiek"]  >= 18, uzytkownicy )))

# print(uzytkownicy2)

uzytkownicy3 = [ u["imie"].upper() for u in uzytkownicy if u["wiek"] >= 18 ]

print(uzytkownicy3)
