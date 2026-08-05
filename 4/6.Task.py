# Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
# Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest "prawdziwy"
# (niepusty) i wyświetl odpowiedni komunikat.



text = input()

is_truthy = bool(text)

if is_truthy:
    print("Good job")
else:
    print("Good")

