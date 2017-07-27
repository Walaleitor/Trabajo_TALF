import turtle

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


##Se logro hacer que la lista generara otra lista con la regla exactamente1,
#falta hacer que dibuje muchas mas veces


def  regla_exactamente1(lista):
    dibujador = []
    dibujador2 = []

    size = len(lista)
    print (lista)
    for i in range(50):
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
        dibujador2.append(dibujador)
        lista = dibujador
        dibujador = []
        dibujar_turtle(dibujador2)



def regla_110(lista):
    dibujador = []
    dibujador2 = []
    size = len(lista)
    print (lista)
    for i in range(50):
        for i in range(size):
            if i == size -3:
                if int(lista[size-3]) + int(lista[size-2]) + int(lista[size-1]) == 2:
                    dibujador.append(1)
                elif int(lista[size-3]) + int(lista[size-2]) + int(lista[size-1]) == 1:
                    if lista[i] == "1":
                        dibujador.append(0)
                    else:
                        dibujador.append(1)
                else:
                    dibujador.append(0)

            elif i == size -2:
                if int(lista[size-2]) + int(lista[size-1]) + int(lista[0]) == 2:
                    dibujador.append(1)
                elif int(lista[size-2]) + int(lista[size-1]) + int(lista[0]) == 1:
                    if lista[i] == "1":
                        dibujador.append(0)
                    else:
                        dibujador.append(1)
                else:
                    dibujador.append(0)


            elif i == size -1:
                if int(lista[-1]) + int(lista[0]) + int(lista[1]) == 2:
                    dibujador.append(1)
                elif int(lista[-1]) + int(lista[0]) + int(lista[1]) == 1:
                    if lista[i] == "1":
                        dibujador.append(0)
                    else:
                        dibujador.append(1)
                else:
                    dibujador.append(0)


            else:
                if int(lista[i]) + int(lista[i+1]) + int(lista[i+2]) == 2:
                    dibujador.append(1)
                elif int(lista[i]) + int(lista[i+1]) + int(lista[i+2]) == 1:
                    if lista[i] == "1":
                        dibujador.append(0)
                    else:
                        dibujador.append(1)
                else:
                    dibujador.append(0)


        print(dibujador)
        dibujador2.append(dibujador)
        dibujar_turtle(dibujador2)
        lista = dibujador
        dibujador = []


def dibujar_turtle(Lista):
    anchodelapiz = 3
    contador_filas = 0
    rango_fila = range(len(Lista[0]))

    #instanciando largo y ancho y velosidad del trasador
    turtle.screensize(5000, 5000, "white")
    turtle.tracer(0, 0)
    turtle.resizemode("auto")


    #crea objeto ventana para facilitar su uso
    ventana = turtle.Screen()
    ventana.bgcolor("lightgreen")
    ventana.title("Automata Celular - Regla exactamente 1")

    #crea el lapiz
    lapiz = turtle.Turtle()
    lapiz.color("blue")
    lapiz.pensize(anchodelapiz)
    lapiz.hideturtle()
    lapiz.speed(0)

    #Dos for anidados que divida las listas en sus elementos mas pequeños
    for fila in Lista:

        for i in rango_fila:

            if fila[i] == 1:
                #Si el caracter es 1 , escribe una cantidad x pixeles hacia la derecha
                lapiz.fd(anchodelapiz)
                print(lapiz.pos())
            else:
                #En el caso que el caracter es 0, el lapiz se sube y se mueve una cantidad x de pixeles para luego se rbajado
                lapiz.penup()
                lapiz.fd(anchodelapiz)
                lapiz.pendown()
                print(lapiz.pos())
        #Una vez finalizado el dibujo de una linea, el lapiz vuelve a la posicion inicial pero x pixeles mas abajo
        contador_filas += -anchodelapiz
        lapiz.penup()
        lapiz.goto(0,contador_filas)
        lapiz.pendown()
