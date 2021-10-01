#encoding:UTF-8
import random
import time

opcionesJuego = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock", "Ver Puntaje", "Salir del Juego"]


partidasPC=0
partidasUsuario=0
partidasEmpate=0
estado = True



def porcentaje():
    x =0
    partidasTotal = partidasPC+partidasUsuario
    if partidasTotal > 0:
        x = (partidasUsuario/partidasTotal) * 100
    return round(x,2)

def muestraPuntaje():
    print ("")
    print ("===Puntajes Obtenidos=== ")
    print ("Usuario: ", partidasUsuario)
    print ("Pc: ", partidasPC)
    print ("Empates: ", partidasEmpate)
    print ("Porcentaje de Mis victorias: ", porcentaje(), "%")
    print ("--------------------")

def pcDecision():
    return random.randrange(1, 5)

def imprimeOpciones():
    print("")
    print("*** A JUGAR ****")
    for o in  opcionesJuego:
        print(str(opcionesJuego.index(o)+1)+"=> "+o)

def devuelvePoder(pc, mi):
    mensajes = {
        "13": "Piedra aplasta Tijera",
        "14": "Piedra aplasta Lagarto",
        "21": "Papel envuelve Piedra",
        "25": "Papel desautoriza Spock",
        "32": "Tijera corta Papel",
        "34": "Tijera decapita Lagarto",
        "42": "Lagarto devora Papel",
        "45": "Lagarto envenena Spock",
        "51": "Spock vaporiza Piedra",
        "53": "Spock rompe Tijera"
    }
    return  mensajes[str(pc)+""+str(mi)]


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

while estado :
    opcionPc = pcDecision()
    imprimeOpciones()
    opcionMi = miDecision()
    if opcionMi == 6:
        muestraPuntaje()
        time.sleep(2.4)
    elif opcionMi == 7:
        muestraPuntaje()
        time.sleep(2.4)
        print("Bye :)")
        estado = False
    else:
        gana= int(ganador(opcionPc, opcionMi))
        print("----------------")
        if gana==-1:
            partidasPC+=1
            print("Gana PC=>" + devuelvePoder(opcionPc, opcionMi))
        elif gana==0:
            partidasEmpate+=1
            print("Empate=> "+opcionesJuego[opcionMi-1])
        else:
            partidasUsuario+=1
            print("Ganaste=>" + devuelvePoder(opcionMi, opcionPc))
        print("-----------------")
        time.sleep(2.4)
