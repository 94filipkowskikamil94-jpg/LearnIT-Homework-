""" Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion
 imiona =["anna", "piotr", "kasia"] 
 w listę imion pisanych wielką literą."""

imiona = ["anna", "piotr", "kasia"] 
imiona_v2 = list(map(lambda x: x.upper(), imiona))

print(imiona_v2)