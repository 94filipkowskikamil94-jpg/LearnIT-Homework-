#Analiza stringa: Utwórz zmienną z łańcuchem znaków " Python jest super! "
#.Wykonaj następujące działania i wyświetl wynik każdego kroku:Usuń zbędne białe znaki na początku i na końcu. 
#Przekształć cały ciąg na małe litery. Zamień słowo "super" na "świetny". Wyświetl na ekranie znak pod indeksem 4 .


Task =" Python jest super! "
Task1 =Task.strip()
Task2 =Task1.lower()
Task3 =Task.replace("super!", "świetny")
Task4 =Task[4]

print(Task)
print(Task1)
print(Task2)
print(Task3)
print(Task4)