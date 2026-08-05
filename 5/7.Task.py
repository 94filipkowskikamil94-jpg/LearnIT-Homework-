# Tylko samogłoski: Poproś użytkownika o zdanie. Użyj pętli for oraz instrukcji continue ,
# aby wyświetlić tylko samogłoski z tego zdania. (Wskazówka: if litera not in
# "aeiouy": continue 

sentence = input("Enter your sentence: ")
not_word = "aeiouy"

for i in sentence:
    if sentence not in not_word:
        continue
print(i)