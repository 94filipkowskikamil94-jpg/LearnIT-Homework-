"""Import z CSV: Napisz program, który odczytuje plik produkty.csv i oblicza sumę cen
wszystkich produktów. Użyj csv.DictReader , aby łatwiej odwoływać się do kolumn po
nazwach"""

import csv
suma = 0
with open("produkty.csv", "r", encoding="utf-8") as plik:
    dane = csv.DictReader(plik)
    for wiersz in dane:
        suma += float(wiersz["cena"])

print(f"Łączna wartość produktów to: {suma} zł")