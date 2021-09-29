#encoding:UTF-8
import random

opcionesJuego = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock", "Salir del Juego"]
def pcDecision():
    return random.randrange(1, 5)

def imprimeOpciones():
    for o in  opcionesJuego:
        print(str(opcionesJuego.index(o)+1)+")"+o)

def miDecision():
    opcion =""
    while opcion=="":
        opcion = input("Que eliges: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion<1 or opcion>opcionesJuego.__len__() :
                opcion=""
        else:
            opcion=""
    return opcion

def ganador(pc, mi):
    ganador=""
    if(mi==1 and (pc ==3 or pc==4)):
        ganador=1
    elif(mi==2 and (pc ==5 or pc==1)):
        ganador=1
    elif (mi == 3 and (pc == 2 or pc == 4)):
        ganador = 1
    elif(mi==4 and (pc ==2 or pc==5)):
        ganador=1
    elif (mi == 5 and (pc == 3 or pc == 1)):
        ganador = 1
    elif (mi == pc):
        ganador = 0
    else:
        ganador=-1
    return  ganador

while True: 
    opcionPc = pcDecision()
    imprimeOpciones()
    opcionMi = miDecision()
    if opcionMi == 6:
        print("Nos vemos!")
        break

    print("Tu eliges: ", opcionesJuego[opcionMi-1])
    print("PC eligio: ", opcionesJuego[opcionPc-1])
    print("...")

    gana= int(ganador(opcionPc, opcionMi))

    if gana==-1:
        print("Gana PC=>")
    elif gana==0:
        print("Empate")
    else:
        print("Ganaste=>")

    again = input("Jugamos de nuevo? Si/No: ")
    if 'No' in again:
        print("Nos vemos!")
        break
