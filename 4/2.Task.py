# Identyfikator obiektu: Utwórz trzy zmienne ( a , b , c ) z tą samą wartością 256 . Sprawdź
# i wyświetl ich id() . Następnie utwórz trzy zmienne z wartością 257 i również sprawdź ich
# # id() . Czy widzisz różnicę w zachowaniu Pythona? Wyjaśnij dlaczego w komentarzu

print()

a = 256
b = 256
c = 256

print(f"a: {id(a)}") 
print(f"b: {id(b)}") 
print(f"c: {id(c)}") 
print()

a = 257
b = 257
c = 257

print(f"a: {id(a)}") 
print(f"b: {id(b)}") 
print(f"c: {id(c)}") 
print()

# Liczby od -5 do 256 są zapamiętane w jednym miejscu w pamięci (mają to samo id).
# Dla 257 Python tworzy za każdym razem nowy obiekt, dlatego ich id() mogą być różne.