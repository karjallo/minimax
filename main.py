from random import randint, sample
from funciones import (presentacion, configuracion, crear_tablero, imprimir_juego, estado_juego, game_over, posibles_movimientos, minimax, pedir_movimiento,
                       validar_movimiento, mover, actualizar_tablero)


DIMENSION = 6
PROFUNDIDAD = 10
MAX_TURNOS = 30
MOV = [[1, 0], [-1, 0], [0, 1], [0, -1]]

presentacion()
jugador = " "
while jugador != "g" and jugador != "r":
     jugador = input("Quien sos? Para Therian Gato escribe G, para Therian Raton escribe R: ").lower()

tablero, posicion_gato, posicion_raton = crear_tablero(DIMENSION)
imprimir_juego(tablero)

turno = 0
while estado_juego(posicion_gato, posicion_raton, turno, MAX_TURNOS) == 0:

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

            minimax(posicion_raton, posicion_gato, DIMENSION, PROFUNDIDAD, False)
            pass


if estado_juego(posicion_gato, posicion_raton, MAX_TURNOS) == 1:
    ganador = "g"
else:
    ganador = "r"

game_over(ganador, jugador)

