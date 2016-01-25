
import numpy
dzienniczek ={'Jan':[4,3,5,3],
                'Anna':[4,5,4,4],
                'Patrycja':[4,5,4,3],
                'Adam':[5,5,3,3],
                'Katarzyna':[3,3,4,3] }
def menu():
    print("""
        Dzienniczek ver 1.0
        [1] wpisz ocene
        [2] ocena na zaliczenie
        [3] usun wpis
        [4] wyjscie
        """)
    wybor = rav_input("\n wybierz opcje: ")
    if (wybor == "1"):
        def wpisz():
            imie= input("imie studenta")
            ocena = iput("podaj ocene")
            if imie in dzienniczek:
                dzienniczek[imie].append(float(ocena))
                print("dodano ocene")
            else:
                print("taka osoba nie istnieje")
    elif (wybor=="2"):
        def obl_srednia():
            for losowa in dzienniczek:
                lista_ocen =dzienniczek[losowa]
                srednia=nu.mean(lista_ocen)
                print ("ta osoba ma srednia:")
    elif (wybor == "3"):
        print ("usun wpis")
    elif (wybor=="4"):
        exit()
    else:
        print ("podaj inna liczbe")

while True:
    menu()
