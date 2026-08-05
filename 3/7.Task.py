# Niemutowalność krotki:
# Utwórz krotkę punkt = (10, 20, 30) .
# Spróbuj zmienić pierwszy element krotki на 15 .
# Wyjaśnij w komentarzu do kodu, dlaczego wystąpił błąd

point = (10, 20, 30)

if isinstance(point, tuple):
    print("This is tuple , it cant be change")

else:
    point[0] = 15
    print("This is a list")




