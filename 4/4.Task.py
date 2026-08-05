# Formatowanie print() : Napisz program, który wyświetli listę zakupów:
# "jajka,mleko,chleb" . Użyj funkcji print() z trzema argumentami tekstowymi i
# odpowiednio ustawionym parametrem sep .

zakupy = ["jajka", "mleko", "chleb"]
print(*zakupy, sep=",")