from random import randint, sample
from funciones import (presentacion, crear_tablero, imprimir_juego, estado_juego, game_over, posibles_movimientos, minimax, pedir_movimiento,
                       validar_movimiento, mover, actualizar_tablero)

def presentacion():
    print('''
    Te despiertas en medio de un extraño laboratorio subterráneo. Las paredes están cubiertas de códigos garabateados, pantallas parpadeantes y… queso. Mucho queso. Frente a ti,
    una científica misteriosa —que claramente se parece a la versión cyborg de Marie Curie— dice con voz robótica:

    "Solo uno sobrevivirá en este laberinto de decisiones. ¿El astuto therian ratón?
    ¿O el implacable therian gato? Tú, aprendiz de estratega, tienes que decidir cómo se juega esta historia."
    ''')

def crear_tablero(dimension):
    tablero = []
    for filas in range(dimension):
        fila = []
        for columnas in range(dimension):
            fila.append(0)
        tablero.append(fila)
    posicion_gato = [randint(0, dimension - 1), randint(0,dimension - 1)]
    posicion_raton = [randint(0, dimension - 1), randint(0,dimension - 1)]
    while posicion_raton == posicion_gato:
        posicion_raton = [randint(0,  dimension - 1), randint(0, dimension -1)]
    tablero[posicion_raton[0]][posicion_raton[1]] = 1
    tablero[posicion_gato[0]][posicion_gato[1]] = 2
    
    return tablero, posicion_raton, posicion_gato

def estado_juego(posicion_raton, posicion_gato, turno, turno_win_raton):
    if posicion_gato == posicion_raton:
        return 2
    elif turno >= turno_win_raton*2:
        return 1
    return 0  

def game_over(ganador, jugador):
    if jugador == ganador:
        print("Ganaste!")
        if ganador == "g":
            print("Devoraste al therian raton")
        else:
            print("Has logrado huir del therian gato")
    else:
        print("Perdiste!")
        if ganador == "g":
            print("Has sido devorado por un therian gato")
        else:
            print("El therian raton logro escapar")

def imprimir_juego(tablero, turno):
    print(f"turno: {turno}")
    print()
    for filas in tablero:
        for columna in filas:
            if columna == 0:
                print("|  ", end=" ")
            elif columna == 1:
                print("| G", end=" ")
            else:
                print("| R", end=" ")
        print("|")

def posibles_movimientos(posicion_actual, dimension, movimientos_posibles):
    movimientos = []
    for mov in movimientos_posibles:
        if validar_movimiento(posicion_actual, mov, dimension):
            movimientos.append(mov)
    return movimientos


def distancia_manhattan(posicion_gato, posicion_raton):
    dif_filas = abs(posicion_gato[0] - posicion_raton[0])
    dif_columnas = abs(posicion_gato[1] - posicion_raton[1])
    return dif_filas + dif_columnas  

def pedir_movimiento():
    direccion = input("en que direccion deseas moverte? w, a, s, d?: ")
    while direccion not in ["w", "a", "s", "d"]:
        print("incorrecto, ingrese de nuevo")
        direccion = input("en que direccion deseas moverte? w, a, s, d?: ")
    if direccion == "w":
        movimiento = [-1, 0]
    elif direccion == "s":
        movimiento = [1, 0]
    elif direccion == "a":
        movimiento = [0, -1]
    elif direccion == "d":
        movimiento = [0, 1]  
    return movimiento

def validar_movimiento(posicion_animal, movimiento_a_realizar, dimension):
    i = posicion_animal[0] + movimiento_a_realizar[0]
    j = posicion_animal[1] + movimiento_a_realizar[1]
    if i < 0 or i >= dimension or j < 0 or j >= dimension:
        return False
    else:
        return True
    
def mover(posicion_animal, movimiento_a_realizar):
    i = posicion_animal[0] + movimiento_a_realizar[0]
    j = posicion_animal[1] + movimiento_a_realizar[1]
    return [i, j]

def actualizar_tablero(tablero, antigua_posicion, nueva_posicion, valor_a_modificar):
    tablero[antigua_posicion[0]][antigua_posicion[1]] = 0
    tablero[nueva_posicion[0]][nueva_posicion[1]] = valor_a_modificar
    return tablero

def minimax(posicion_raton, posicion_gato, dimension, profundidad, movs, es_maximizador):

    distancia = distancia_manhattan(posicion_gato, posicion_raton)
    if posicion_gato == posicion_raton:
        return -1000
    elif profundidad <= 0:
        return 1000
    else:
        puntaje = distancia

    if es_maximizador:
        mejor_puntaje = float('-inf')
        movimientos = posibles_movimientos(posicion_raton, dimension, movs)
        for movimiento in movimientos:
           #simular movimiento
           #mover()
           puntaje = minimax(tablero, profundidad + 1, False)
           # deshacer_movimiento()
           mejor_puntaje = max(puntaje, mejor_puntaje)
        return mejor_puntaje

   # si es el turno del gato (minimizador)
    else:
        mejor_puntaje = float('inf')
        movimientos = posibles_movimientos(posicion_gato, len(tablero[0]), len(tablero))
        for movimiento in movimientos:
            #simular movimiento
            #mover()
            puntaje = minimax(tablero, profundidad + 1, True)
            # deshacer_movimiento()
            mejor_puntaje = min(puntaje, mejor_puntaje)
        return mejor_puntaje

DIMENSION = 6
PROFUNDIDAD = 10
MAX_TURNOS = 30
MOV = [[1, 0], [-1, 0], [0, 1], [0, -1]]

presentacion()
jugador = " "
while jugador != "g" and jugador != "r":
     jugador = input("Quien sos? Para Therian Gato escribe G, para Therian Raton escribe R: ").lower()

tablero, posicion_raton, posicion_gato = crear_tablero(DIMENSION)
imprimir_juego(tablero)

turno = 0
while estado_juego(posicion_raton, posicion_gato, turno, MAX_TURNOS) == 0:

    ############## TURNO RATON #############
    if turno % 2 > 0:
        ########### JUGADOR  #############
        if jugador == "r":
            while True:
                movimiento = pedir_movimiento()
                if validar_movimiento(posicion_raton, movimiento, DIMENSION) == False:
                    print("movimiento invalido, ingrese nuevamente")
                else:
                    nueva_posicion_raton = mover(posicion_raton, movimiento)
                    break

            tablero = actualizar_tablero(tablero, posicion_raton, nueva_posicion_raton, 2)
            posicion_raton = nueva_posicion_raton
            turno = turno + 1
            imprimir_juego(tablero, turno)

        else:
            ########### MAX #############
            minimax(posicion_raton, posicion_gato, DIMENSION, PROFUNDIDAD, False)
            pass


    ######### TURNO GATO ###########
    else:
        ########### JUGADOR  #############
        if jugador == "g":
            while True:
                movimiento = pedir_movimiento()
                if validar_movimiento(posicion_gato, movimiento, DIMENSION) == False:
                    print("movimiento invalido, ingrese nuevamente")
                else:
                    nueva_posicion_gato = mover(posicion_gato, movimiento)
                    break

            tablero = actualizar_tablero(tablero, posicion_gato, nueva_posicion_gato, 1)
            posicion_gato = nueva_posicion_gato
            turno = turno + 1
            imprimir_juego(tablero, turno)

        else:
            ########### MIN #############
            mejor_movimiento = minimax(posicion_raton, posicion_gato, DIMENSION, PROFUNDIDAD, False)
            tablero = actualizar_tablero(tablero, posicion_gato, mejor_movimiento, 1)
            pass


if estado_juego(posicion_raton, posicion_gato, MAX_TURNOS) == 1:
    ganador = "g"
else:
    ganador = "r"

game_over(ganador, jugador)

