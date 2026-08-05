# Identyfikator po zmianie: Utwórz zmienną x = 10 . Wyświetl jej id() . Następnie
# przypisz do x nową wartość x = x + 1 . Ponownie wyświetl id() . Czy identyfikator się
# # zmienił? Dlaczego? Odpowiedz w komentarzu

x = 10

print(f"{id(x)}")

x = x +1 

print(f"{id(x)}")

# The id() changed because integers are immutable in Python. 
# 'x = x + 1' creates a new object in memory with a new ID.