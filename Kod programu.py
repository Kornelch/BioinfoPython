import numpy
dzienniczek = {'Jan':[4, 5, 4, 5],
                'Ola':[2, 5, 3, 5],
                'Aga':[5, 5, 5, 5],
                'Kamil':[2, 2, 2, 2],
                'Kasia':[5, 5, 3, 5],}

def wpisz():
    imie = input("podaj imie studenta")
    ocena = input("podaj ocene")

    if imie in dzienniczek:
        dzienniczek[imie].append(float(ocena))
        print ("udalo dodac sie ocene")
    else:
        print("taka osoba niestety nie istnieje")

def srednia():
    for imie in dzienniczek:
        lista_ocen = dzienniczek[imie]
        srednia = nu.mean(lista_ocen)
        print("srednia dla tego studenta to: ",srednia)

def menu():
    print("""
            Witaj w menu dzienniczka:
            [1] Wpisz ocenę
            [2] Ocena na zaliczenie
            [3] Usuń wpis
            [4] Wyjscie
             """)

    wybor =input("\n wybierz opcje: ")
    print(wybor)

    if wybor == "1":
        wpisz()
    elif wybor =="2":
        print ("wybrales opcję 2 - ocena na zaliczenie")
    elif wybor =="3":
        print ("wybrales opcję 3 - usuń wpis")
    elif wybor =="4":
        print ("wybrales opcję 4 - wyjscie")
        exit()
    else:
        print ("nie ma takiej opcji")
while True:
    menu()
