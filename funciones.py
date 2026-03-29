from random import randint

def presentacion():
    print('''
    Te despiertas en medio de un extraño laboratorio subterráneo. Las paredes están cubiertas de códigos garabateados, pantallas parpadeantes y… queso. Mucho queso. Frente a ti,
    una científica misteriosa —que claramente se parece a la versión cyborg de Marie Curie— dice con voz robótica:

    "Solo uno sobrevivirá en este laberinto de decisiones. ¿El astuto therian ratón?
    ¿O el implacable therian gato? Tú, aprendiz de estratega, tienes que decidir cómo se juega esta historia."
    ''')

def crear_tablero(dimension):
    tablero = []
    for y in range(dimension):
        fila = []
        for x in range(dimension):
            fila.append(0)
        tablero.append(fila)

    posicion_gato = [randint(0,filas - 1), randint(0,columnas - 1)]
    posicion_raton = [randint(0,filas - 1), randint(0,columnas - 1)]

    while posicion_raton == posicion_gato:
        posicion_raton = [randint(0, filas - 1), randint(0, columnas -1)]

    tablero[posicion_raton[0]][posicion_raton[1]] = 1
    tablero[posicion_gato[0]][posicion_gato[1]] = 2

    
    return tablero, posicion_gato, posicion_raton

def estado_juego(posicion_gato, posicion_raton, turno, turno_win_raton):
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
        fila = posicion_actual[0] + movimientos_posibles[0]
        columna = posicion_actual[1] + movimientos_posibles[1]
        if fila < dimension and fila >= 0 and columna < dimension and columna >= 0:
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

def minimax(posicion_raton, posicion_gato, dimension, profundidad, es_maximizador):

    distancia = distancia_manhattan(posicion_gato, posicion_raton)

    if posicion_gato == posicion_raton:
        puntaje = -1000
    elif profundidad <= 0:
        puntaje = 1000
    else:
        puntaje = distancia

    if es_maximizador:
        mejor_puntaje = float('-inf')
        movimientos = posibles_movimientos(posicion_raton, len(tablero[0]), len(tablero))

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