"""  Dekorator logujący: Napisz dekorator @loguj , który przed wywołaniem udekorowanej
funkcji wypisze komunikat Uruchamiam funkcję [nazwa_funkcji]... , a po jej
zakończeniu Zakończono funkcję [nazwa_funkcji]. """

def test(Próba):
    def dekorowanie():
        print("Cześć!")
        Próba()   
        print("Dobranoc")

    return dekorowanie



@test
def moja_funkcja():
    print("Jestem TUTAJ !")

moja_funkcja()
    