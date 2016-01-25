# Kasia, Mateusz 

import numpy

dzienniczek = {'Jan':[4,5,4,3],
                'Anna':[2,3,3,2],
                'Adam':[4,3,3,3],
                'Marian':[5,5,2,3],
                }
def wpisz_ocene():
    imie = input('podaj imię:')
    ocena = input('podaj ocene')
    if imie in dzienniczek:
        dzienniczek[imie].append(float(ocena))
        print('dodano ocene')
    else:
        print('brak takiego imienia')

def zaliczenie():
    for imie in dzienniczek:
        oceny = dzienniczek[imie]
        srednia = nu.mean(oceny)
        print(imie + srednia)


def menu():
    print("""
        Dzienniczek ver 1.0
        [1] wpisz ocenę
        [2] ocena na zaliczenie
        [3] usuń wpis
        [4] wyjscie
         """)
    wybor =input('wybierz opcje:')
    if wybor == "1":
       def wpisz_ocene():
    elif wybor == "2":
        def zaliczenie():
    elif wybor == "3":
        print("dobrze")
    elif wybor == "4":
        exit()
    else:
        print("błedny wybor")

while True:
    menu()
