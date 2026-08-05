# Mini-projekt "Formater danych": Napisz program, który poprosi użytkownika o jego imię i
# nazwisko w jednej linii (np. " jan kowalski "). Program powinien:
# Oczyścić zbędne białe znaki.
# Sprawić, aby każde słowo zaczynało się wielką literą (metoda .title() ).
# Wyświetlić sformatowane dane oraz ich długość.

start = input("Tell me your name: ")
clean_start = start.strip().title()

print(f"Name: {clean_start}")
print(f"Len: {len(clean_start)}")
