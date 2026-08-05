""" Eksport do CSV: Masz listę słowników: produkty = [{"nazwa": "Mleko", "cena":
3.50}, {"nazwa": "Chleb", "cena": 4.20}] . Zapisz te dane do pliku produkty.csv ,
gdzie pierwszy wiersz to nagłówki ("nazwa", "cena").
"""
import csv

produkty = [{"nazwa": "Mleko", "cena": 3.50}, {"nazwa": "Chleb", "cena": 4.20}] 
naglowki = ["nazwa", "cena"]

with open("produkty.csv", "w", encoding="utf-8", newline="") as plik:
    zapisywacz = csv.DictWriter(plik, fieldnames=naglowki)
    zapisywacz.writeheader()
    for produkt in produkty:
        zapisywacz.writerow(produkt)
    