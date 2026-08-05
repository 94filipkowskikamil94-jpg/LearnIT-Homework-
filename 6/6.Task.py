# Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc:
# int) -> None , która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi
# ilosc . Ta funkcja nie powinna niczego zwracać

def wielokrotne_powitanie(imie: str, ilosc:int) -> None:
    for _ in range(ilosc):
        print(f"{imie}!")

wielokrotne_powitanie("Tomek", 4)