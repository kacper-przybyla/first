#Tablica wyników v2
#
#kacper
#07.11.2018

scores = []
choice = None

print("""
    Tablica wyników v2

    0 - wyjdź z programu
    1 - dodaj wynik
    2 - pokaż tablicę wyników

    """)

while choice != "0":
    choice = input("Co chcesz zrobić?: ")

    if choice == "0":
        print("Do widzenia")

    elif choice == "1":
        name = input("Podaj imię: ")
        score = int(input ("Podaj wynik: "))
        entry = (name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
        print("Wynik został dodany\n")

    elif choice == "2":
        print("5 najlepszych wyników: ")
        print("IMIE\tWYNIK")
        for entry in scores:
            name, score = entry
            print(name, "\t", score)
        print("")

    else:
        print("Nie rozumiem komunikatu", choice)
