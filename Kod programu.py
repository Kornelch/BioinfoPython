import numpy

dzienniczek = {'Josefina': [4, 5, 3, 5],
'Henio': [3, 2, 2, 4],
'Bogus': [5, 2, 4, 4],
'Romek': [2, 5, 5, 5],
'Karyna': [2, 2, 3, 2]}

##słownik ^^^^^

def wpisz():
    imie = input("wprowadz imie studenta: ")
    ocenka = input("wprowadz ocene: ")

    if imie in dzienniczek:
        dzienniczek[imie].append(float(ocenka))
##funkcja append to dopisywanie, w nawiasie konwersja ze string na float
##ten if sprawdza czy wprowadzone imie wystepuje w dzienniczku
        print("udalo ci sie dodac ocenke")

    else:
        print("kapa, nie ma takiego studenta")

def srednia():
    for imie in dzienniczek:
        lista_ocen = dzienniczek[imie]
        srednia = nu.mean(lista_ocen)
        print("srednia tego studenta to: ", srednia)

##nu to odwolanie do biblioteki numpy

def usuwanie():


def menu():
##funkcja

    print("""
    dzienniczek
        [1] wpisz ocene
        [2] ocena na zaliczneie
        [3] usun wpis
        [4] wyjscie
    """)

##menu ^

    wybor = input("\n wybierz opcje: ")

    if wybor == "1":
        wpisz()

    elif wybor == "2":
        print("opcja 2")

    elif wybor == "3":
        print("opcja 3")

    elif wybor == "4":
        exit()

    else:
        print("zly przycisk, wybierz inny")

while True:
    menu()
