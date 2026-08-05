""" Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. Powinna ona zwracać listę
wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym
problemie. Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError ,
przekazując do niego tę listę"""

class BladWalidacjiError(Exception):
    pass

def waliduj_haslo(haslo):
    bledy = []
    if len(haslo) < 8:
        bledy.append("Hasło jest za krótkie")
           
    
    ma_wielka = False
    ma_cyfra = False
    
    for litera in haslo:
        if litera.isupper():
            ma_wielka = True
                
    for cyfra in haslo:       
        if cyfra.isdigit():
            ma_cyfra = True 
                     
    
    if bledy:
        raise BladWalidacjiError(bledy)
    
print(f"{waliduj_haslo("We2rt02!")}")
