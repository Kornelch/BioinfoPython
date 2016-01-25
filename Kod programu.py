Patryk:

#import numpy
dzienniczek = {'Jan':[4,5,4,5],
                'Anna':[4,6,1,3],
                'Piotr':[2,2,2,2],
                'Dawid':[3,6,2,3]}
def wybor1():
    imie=input('Podaj imie studenta: ')
    ocena=input('Podaj ocene dla studenta: ')
    if imie in dzienniczek:
        dzienniczek[imie].append(float(ocena))
        print("Dopisano ocene studentowi")
    else:
        print("Brak studenta o podanym imieniu")

def wybor2():
    for imie in dzienniczek:
        lista_ocen=dzienniczek[imie]
        srednia = mean(lista_ocen)
        print(imie + "ma srednia: " + srednia)
def menu():
    print("""Witaj w menu:
        [1]Dopisz ocene studentowi
        [2]Oblicz srednia studentowi
        [3]Usun rekord
        [4]Wyjscie""")
    wybor = input('Twoj wybor: ')
    if wybor == '1':
        wybor1()
    elif wybor =='2':
        wybor2()
        print("Obliczono srednia ocen studenta")
    elif wybor =='3':
        print("Usunieto rekord")
    elif wybor =='4':
        exit()
    else:
        print("Bledny wybor. Sprobuj jeszcze raz")

while True:
    menu()
