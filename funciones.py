def validar(lista):
    contador = 0
    if len(lista) > 10:
        for i in lista:
            if i != "0" and i != "1":
                contador += 1

        if contador > 0:
            lista = []
            print ("vuelva a ingresar la lista")
            return lista

        else:
            print("la lista se ingreso bien")
            return lista
    else:
        lista = []
        print("Ingrese una palabra mayor a 10")
        return lista


##Se logro hacer que la lista generara otra lista con la regla exactamente1
#falta hacer que dibuje muchas mas veces
def exactamente1(lista):
    dibujador = []
    size = len(lista)
    for i in range(size):
        if i == size -3:
            if int(lista[size-3]) + int(lista[size-2]) + int(lista[size-1]) == 1:
                dibujador.append(1)
            else:
                dibujador.append(0)
        elif i == size -2:
            if int(lista[size-2]) + int(lista[size-1]) + int(lista[0]) == 1:
                dibujador.append(1)
            else:
                dibujador.append(0)
        elif i == size -1:
            if int(lista[-1]) + int(lista[0]) + int(lista[1]) == 1:
                dibujador.append(1)
            else:
                dibujador.append(0)
        else:
            if int(lista[i]) + int(lista[i+1]) + int(lista[i+2]) == 1:
                dibujador.append(1)
            else:
                dibujador.append(0)

    print(dibujador)






lista = input("ingresa lista \n")
exactamente1(lista)
