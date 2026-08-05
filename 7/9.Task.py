"""Dekorator z argumentem: Stwórz dekorator @powtorz(n) , który przyjmuje argument n i
powoduje, że udekorowana funkcja zostanie wykonana n razy"""



def powtorz(n):

    def dekorator(funkcja):
      
        def wrapper():
            for _ in range(n):
                funkcja()

        return wrapper

    return dekorator

@powtorz(3)
def nowa():
    print("Siema!")


nowa()