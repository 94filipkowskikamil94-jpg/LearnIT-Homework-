"""Prosty arkusz kalkulacyjny: Używając openpyxl , stwórz plik finanse.xlsx . W
pierwszej kolumnie umieść nazwy wydatków (np. "Czynsz", "Jedzenie"), a w drugiej ich
wartości. W komórce poniżej wartości oblicz i wstaw sumę wszystkich wydatków, używając
formuły Excela (np. =SUM(B1:B2) )."""

from openpyxl import Workbook

wb = Workbook()

ws = wb.active
ws.title = "Wydatki"  

ws.append(["Czynsz", 1500])
ws.append(["Jedzenie", 800])
ws.append(["Suma:", "=SUM(B1:B2)"])

wb.save("finanse.xlsx")

print("Gotowe! Arkusz zapisany.")
