"""Tworzenie struktury folderów: Użyj modułu pathlib , aby napisać skrypt, który tworzy
strukturę folderów: Projekt/src , Projekt/data , Projekt/docs"""

from pathlib import Path

foldery_do_stworzenia = [
    "Projekt/src",
    "Projekt/data",
    "Projekt/docs"
]

for nazwa_folderu in foldery_do_stworzenia:
    
    sciezka = Path(nazwa_folderu)
    
    sciezka.mkdir(parents=True, exist_ok=True)

print("Struktura folderów została utworzona.")