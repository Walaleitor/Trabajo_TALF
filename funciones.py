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





lista = input("ingresa lista \n")
print(validar(lista))
