"""Licznik wywołań: Stwórz domknięcie (closure). Napisz funkcję stworz_licznik() , która
zwraca funkcję. Każde wywołanie zwróconej funkcji powinno zwiększać wewnętrzny licznik i
zwracać jego aktualną wartość"""

def stworz_licznik():

    licznik = 0

    def dodaj():
        nonlocal licznik
        licznik += 1
        return licznik

    return dodaj 

moj_licznik = stworz_licznik()


print(moj_licznik())  
print(moj_licznik())  
print(moj_licznik())  
print(moj_licznik())
print(moj_licznik())  
print(moj_licznik())  
print(moj_licznik())  
print(moj_licznik())