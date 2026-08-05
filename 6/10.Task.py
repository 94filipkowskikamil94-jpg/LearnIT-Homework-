# """Mini-projekt: Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
# Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub
# False :
# Ma co najmniej 8 znaków.
# Zawiera co najmniej jedną wielką literę.
# Zawiera co najmniej jedną cyfrę. Napisz do niej pełną dokumentację (docstring i
# adnotacje)
# """
def sprawdz_haslo(haslo: str) -> bool:
    """
    Sprawdza, czy hasło ma min. 8 znaków, wielką literę i cyfrę.
    """
    # 1. Jeśli za krótkie -> od razu odrzucamy!
    if len(haslo) < 8:
        return False

    ma_wielka = False
    ma_cyfra = False

    # 2. Przeglądamy litera po literze z odpowiednimi wcięciami:
    for litera in haslo:
        if litera.isupper():
            ma_wielka = True
    for cyfra in haslo:       
        if cyfra.isdigit():
            ma_cyfra = True 
            #TUTAJ DODAJEMY CYFRĘ

    # 3. Zwracamy True TYLKO wtedy, gdy OBA warunki są True:
    return ma_wielka and ma_cyfra

print(f"{sprawdz_haslo("wert02!")}")