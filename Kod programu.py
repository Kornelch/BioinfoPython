import numpy
dzienniczek = {'Jan': [4, 5, 3, 5],
                'Anna': [3, 4, 5, 4],
                'Zuzanna': [4, 3, 3, 3],
                'Klaudia': [5, 4, 4, 5]
                }

def wpisz():
    imie = input("wpisz imie")
    ocena = input("podaj ocene")

    if imie in dzienniczek:
        dzienniczek[imie].append(float(ocena))
        print("Dodano ocene")
    else:
        print("Taka osoba nie istnieje")

def obl_srednia():
    for osoba in dzienniczek:
        lista_ocen = dzienniczek[osoba]
        srednia = nu.mean(lista_ocen)
        print(imie, srednia)
def menu():
    print (""" Dzienniczek ver 1.0
        [1] Wpisz ocene
        [2] Ocena na zaliczenie
        [3] Usun wpis
        [4] Wyjscie
        """)
    wybor = input("\n Wybierz opcje:")
    if wybor == "1":
       wpisz()
    elif wybor == "2":
       obl_srednia()
    elif wybor == "3":
        print("wybrales opcje Usun wpis")
    elif wybor == "4":
        exit()
    else :
        print("nie ma takiej opcji")

while True:
    menu()
