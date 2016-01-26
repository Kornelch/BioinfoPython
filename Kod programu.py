dziennik = {'Andrzej':[3,4,4,2],
                'Helena':[2,4,3,1],
                'Piotr':[4,5,4,3],
                'Patryk':[2,3,1,4]}
def wybor1():
    imie=input('Podaj imie studenta: ')
    stopien=input('Podaj ocene: ')
    if imie in dzienniczek:
        dzienniczek[imie].append(float(ocena))
        print("Dopisano ocene ")
    else:
        print("Brak studenta o podanym imieniu")

def wybor2():
    for imie in dzienniczek:
        lista_ocen=dzienniczek[imie]
        srednia = mean(lista_ocen)
        print(imie + "ma srednia: " + srednia)
def menu():
    print("""Witaj w menu:
        [1]Dopisz stopien studentowi
        [2]Oblicz srednia studentowi
        [3]Usun rekord
        [4]Wyjscie""")
    wybor = input('Twoj wybor: ')
    if wybor == '1':
        wybor1()
    elif wybor =='2':
        wybor2()
        print("Obliczono srednia ocen ")
    elif wybor =='3':
        print("Usunieto wpis")
    elif wybor =='4':
        exit()
    else:
        print("Bledny wybor. Sprobuj raz jeszcze")

while True:
    menu()
