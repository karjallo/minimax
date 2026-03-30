from random import randint

def presentacion():
    print('''
    Te despiertas en medio de un extraño laboratorio subterráneo. Las paredes están cubiertas de
    códigos garabateados, pantallas parpadeantes y… queso. Mucho queso. Frente a ti,
    una científica misteriosa —que claramente se parece a la versión cyborg de Marie Curie—
    dice con voz robótica:

    "Solo uno sobrevivirá en este laberinto de decisiones. ¿El astuto therian ratón?
    ¿O el implacable therian gato? Tú, aprendiz de estratega, tienes que decidir cómo se juega."
    ''')


def crear_tablero(dimension):
    tablero = [[0] * dimension for _ in range(dimension)]

    posicion_gato = [randint(0, dimension - 1), randint(0, dimension - 1)]
    posicion_raton = [randint(0, dimension - 1), randint(0, dimension - 1)]
    while posicion_raton == posicion_gato:
        posicion_raton = [randint(0, dimension - 1), randint(0, dimension - 1)]

    tablero[posicion_raton[0]][posicion_raton[1]] = 1   
    tablero[posicion_gato[0]][posicion_gato[1]]  = 2   

    return tablero, posicion_raton, posicion_gato


def imprimir_juego(tablero, turno):
    if turno != 0:
        print(f"Turno: {turno}")
    for fila in tablero:
        for celda in fila:
            if celda == 0:
                print("|  ", end=" ")
            elif celda == 1:
                print("| R", end=" ")
            else:
                print("| G", end=" ")
        print("|")


def estado_juego(posicion_raton, posicion_gato, turno, turno_win_raton):
    if posicion_gato == posicion_raton:
        return 2                         
    elif turno >= turno_win_raton * 2:
        return 1                         
    return 0                             


def game_over(ganador, jugador):
    if jugador == ganador:
        print("\n¡Ganaste!")
        if ganador == "g":
            print("Devoraste al therian ratón.")
        else:
            print("Has logrado huir del therian gato.")
    else:
        print("\n¡Perdiste!")
        if ganador == "g":
            print("Has sido devorado por un therian gato.")
        else:
            print("El therian ratón logró escapar.")


def posibles_movimientos(posicion_actual, dimension, movimientos_posibles):
    return [mov for mov in movimientos_posibles
            if validar_movimiento(posicion_actual, mov, dimension)]


def pedir_movimiento():
    direccion = input("¿En qué dirección deseas moverte? (w/a/s/d): ").lower()
    while direccion not in ["w", "a", "s", "d"]:
        print("Dirección incorrecta, intenta de nuevo.")
        direccion = input("¿En qué dirección deseas moverte? (w/a/s/d): ").lower()

    mapa = {"w": [-1, 0], "s": [1, 0], "a": [0, -1], "d": [0, 1]}
    return mapa[direccion]


def validar_movimiento(posicion_animal, movimiento_a_realizar, dimension):
    i = posicion_animal[0] + movimiento_a_realizar[0]
    j = posicion_animal[1] + movimiento_a_realizar[1]
    return 0 <= i < dimension and 0 <= j < dimension


def mover(posicion_animal, movimiento_a_realizar):
    return [posicion_animal[0] + movimiento_a_realizar[0],
            posicion_animal[1] + movimiento_a_realizar[1]]


def actualizar_tablero(tablero, antigua_posicion, nueva_posicion, valor):
    tablero[antigua_posicion[0]][antigua_posicion[1]] = 0
    tablero[nueva_posicion[0]][nueva_posicion[1]] = valor
    return tablero


def distancia_manhattan(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])

def minimax(posicion_raton, posicion_gato, dimension, profundidad, movs, es_maximizador):

    if posicion_gato == posicion_raton:
        return -1000

    if profundidad <= 0:
        return distancia_manhattan(posicion_gato, posicion_raton)

    if es_maximizador:
        mejor_puntaje = float('-inf')
        for movimiento in posibles_movimientos(posicion_raton, dimension, movs):
            nueva_pos_raton = mover(posicion_raton, movimiento)
            puntaje = minimax(nueva_pos_raton, posicion_gato,
                              dimension, profundidad - 1, movs, False)
            mejor_puntaje = max(puntaje, mejor_puntaje)
        return mejor_puntaje

    else:
        mejor_puntaje = float('inf')
        for movimiento in posibles_movimientos(posicion_gato, dimension, movs):
            nueva_pos_gato = mover(posicion_gato, movimiento)
            puntaje = minimax(posicion_raton, nueva_pos_gato,
                              dimension, profundidad - 1, movs, True)
            mejor_puntaje = min(puntaje, mejor_puntaje)
        return mejor_puntaje



DIMENSION  = 6
PROFUNDIDAD = 10
MAX_TURNOS = 30
MOV = [[1, 0], [-1, 0], [0, 1], [0, -1]]

presentacion()
jugador = ""
while jugador not in ["g", "r"]:
    jugador = input("¿Quién sos? Para Therian Gato escribe G, para Therian Ratón escribe R: ").strip().lower()

tablero, posicion_raton, posicion_gato = crear_tablero(DIMENSION)
turno = 0
imprimir_juego(tablero, turno)

while estado_juego(posicion_raton, posicion_gato, turno, MAX_TURNOS) == 0:

    if turno % 2 != 0:

        if jugador == "r":
            while True:
                movimiento = pedir_movimiento()
                if not validar_movimiento(posicion_raton, movimiento, DIMENSION):
                    print("Movimiento inválido, ingresá de nuevo.")
                else:
                    nueva_posicion_raton = mover(posicion_raton, movimiento)
                    break

        else:
            mejor_puntaje   = float('-inf')
            nueva_posicion_raton = posicion_raton

            for movimiento in posibles_movimientos(posicion_raton, DIMENSION, MOV):
                pos_simulada = mover(posicion_raton, movimiento)
                puntaje = minimax(pos_simulada, posicion_gato,
                                  DIMENSION, PROFUNDIDAD - 1, MOV, False)
                if puntaje > mejor_puntaje:
                    mejor_puntaje        = puntaje
                    nueva_posicion_raton = pos_simulada

        tablero = actualizar_tablero(tablero, posicion_raton, nueva_posicion_raton, 1)
        posicion_raton = nueva_posicion_raton
        turno = turno + 1
        imprimir_juego(tablero, turno)

    else:
        if jugador == "g":
            while True:
                movimiento = pedir_movimiento()
                if not validar_movimiento(posicion_gato, movimiento, DIMENSION):
                    print("Movimiento inválido, ingresá de nuevo.")
                else:
                    nueva_posicion_gato = mover(posicion_gato, movimiento)
                    break

        else:
            mejor_puntaje  = float('inf')
            nueva_posicion_gato = posicion_gato

            for movimiento in posibles_movimientos(posicion_gato, DIMENSION, MOV):
                pos_simulada = mover(posicion_gato, movimiento)
                puntaje = minimax(posicion_raton, pos_simulada,
                                  DIMENSION, PROFUNDIDAD - 1, MOV, True)
                if puntaje < mejor_puntaje:
                    mejor_puntaje       = puntaje
                    nueva_posicion_gato = pos_simulada

        tablero = actualizar_tablero(tablero, posicion_gato, nueva_posicion_gato, 2)
        posicion_gato = nueva_posicion_gato
        turno = turno + 1
        imprimir_juego(tablero, turno)

estado_final = estado_juego(posicion_raton, posicion_gato, turno, MAX_TURNOS)
ganador = "r" if estado_final == 1 else "g"
game_over(ganador, jugador)
