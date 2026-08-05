# 8. Obliczanie wieku psa: Przyjmuje się, że pierwszy rok życia psa to 15 ludzkich lat, drugi to
# 9, a każdy kolejny to 5. Napisz program, który pyta o wiek psa w latach, a następnie oblicza
# i wyświetla jego wiek w "ludzkich" latach.

age_dog = float(input("How old are your dog ?"))

if age_dog < 1:
    print(f"First version: {age_dog * 15}")
elif age_dog >=1:
    print(f"First version: {age_dog * 9}")
elif age_dog >=2:
    print(f"First version: {age_dog * 5}")


