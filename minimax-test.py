from random import randint, sample

def imprimir_tablero(raton, gato):
    if turno != 0:
        print(f"Turno: {turno}")

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if raton == [i, j]:
                print("| R", end=" ")
            elif gato == [i, j]:
                print("| G", end=" ")
            else:
                print("|  ", end=" ")
        print("|")


def mejor_movimiento(raton, gato, es_maximizador): 
    if es_maximizador:
        mejor_val = -float("inf")
        mejor = raton
        for mov in posibles_movimientos(raton):
            val = minimax(mov, gato, PROFUNDIDAD, False)  # ✅ mov=ratón, gato=gato
            if val > mejor_val: 
                mejor_val = val
                mejor = mov
        return mejor
    else:
        mejor_val = float("inf")
        mejor = gato
        for mov in posibles_movimientos(gato): 
            val = minimax(raton, mov, PROFUNDIDAD, True)  # ✅ raton=ratón, mov=gato
            if val < mejor_val: 
                mejor_val = val
                mejor = mov
        return mejor


def minimax(raton, gato, profundidad, es_maximizador):
    if raton == gato:
        return -float("inf")
    if profundidad == 0:
        return abs(raton[0] - gato[0]) + abs(raton[1] - gato[1])

    if es_maximizador: 
        mejor_val = -float("inf")
        for mov in posibles_movimientos(raton):
            val = minimax(gato, mov, profundidad - 1, False)  # ✅
            mejor_val = max(mejor_val, val)
        return mejor_val
    else:
        mejor_val = float("inf")
        for mov in posibles_movimientos(gato):
            val = minimax(mov, gato, profundidad - 1, True)  # ✅
            mejor_val = min(mejor_val, val)
        return mejor_val


def posibles_movimientos(posicion_actual):
    posibles = []
    for movimiento in MOVS:
        if validar_movimiento(posicion_actual, movimiento):
            nueva_pos = [posicion_actual[0] + movimiento[0],
                         posicion_actual[1] + movimiento[1]]
            posibles.append(nueva_pos)
    return posibles


def validar_movimiento(posicion_animal, movimiento_a_realizar):
    i = posicion_animal[0] + movimiento_a_realizar[0]
    j = posicion_animal[1] + movimiento_a_realizar[1]
    return 0 <= i < DIMENSION and 0 <= j < DIMENSION


MAX_TURNOS = 20
DIMENSION = 6
PROFUNDIDAD = 6
MOVS = [[0, 1], [0, -1], [-1, 0], [1, 0]]

raton = [0, 0]
gato = [DIMENSION - 1, DIMENSION - 1]
turno = 0


while turno <= MAX_TURNOS:

    if turno == 0:
        imprimir_tablero(raton, gato)

    # turno raton
    raton = mejor_movimiento(raton, gato, True)
    imprimir_tablero(raton, gato)
    if raton == gato:
        print("el Gato ha ganado")
        break
    
    gato = mejor_movimiento(raton, gato, False)
    imprimir_tablero(raton, gato)
    if raton == gato:
        print("el Gato ha ganado")
        break

    turno = turno + 1

if turno >= MAX_TURNOS:
    print("gano el raton")