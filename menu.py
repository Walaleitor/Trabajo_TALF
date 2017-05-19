import os
from funciones import regla_110, regla_exactamente1, validar

def menu():

    print ("Menu Trabajo 1 de Talf")
    print ("Ingrese alguna de las siguentes opciones")
    print ("\t 1 - Regla Exactamente 1")
    print ("\t 2 - Regla de 101")
    print ("\t 9 - Salir")



while True:
    lista = input("ingrese la entrada para el automata\n")
    print ("\t Ya ingreso el automata pulse \n")
    menu()
    opcion  = int(input("ingrese su opcion\n"))
    os.system("cls")

    if opcion == 1:
        print("Regla Exactamente 1")
        regla_exactamente1(lista)

    elif opcion == 2:
        print("Regla de 101")
        regla_110(lista)
    elif opcion == 9:
        break
    else:
        print("Ingrese una opcion valida:")
