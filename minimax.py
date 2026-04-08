from random import sample


def minimax(raton, gato, profundidad, es_maximizador):
    if raton == gato:
        return -100 - profundidad
    if profundidad == 0:
        return distancia_manhattan(raton, gato)
    
    # turno raton
    if es_maximizador:
        mejor_val = -float("inf")
        for mov in posibles_movimientos(raton):
            val = minimax(mov, gato, profundidad - 1, False)
            mejor_val = max(mejor_val, val) 
        return mejor_val
    # Turno gato
    else:
        mejor_val = float("inf")
        for mov in posibles_movimientos(gato):
            val = minimax(raton, mov, profundidad - 1, True)
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


def distancia_manhattan(raton, gato):
    return abs(raton[0] - gato[0]) + abs(raton[1] - gato[1])


def imprimir_tablero(raton, gato):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if raton == [i, j]:
                print("| R", end=" ")
            elif gato == [i, j]:
                print("| G", end=" ")
            else:
                print("|  ", end=" ")
        print("|")


MAX_TURNOS = 20
DIMENSION = 6
PROFUNDIDAD = 10
MOVS = [[0, 1], [0, -1], [-1, 0], [1, 0]]

todas_las_celdas = []
for i in range(DIMENSION):
    for j in range(DIMENSION):
        todas_las_celdas.append([i, j])
raton, gato = sample(todas_las_celdas, 2)
turno = 1


while turno <= MAX_TURNOS:
    print("##############################")
    print(f"turno: {turno}")

    # ── turno ratón ──────────────────────────────────────────────
    mejor_val = -float("inf")
    mejores = []
    for mov in posibles_movimientos(raton):
        val = minimax(mov, gato, PROFUNDIDAD, False)
        if val > mejor_val:
            mejor_val = val
            mejores = [mov]
        elif val == mejor_val:
            mejores.append(mov)
    # entre los mejores, elige el más lejano al gato
    raton = mejores[0]
    for mej in mejores:
        if distancia_manhattan(mov, gato) > distancia_manhattan(raton, gato):
            raton = mej

    print()
    print("mueve raton")
    imprimir_tablero(raton, gato)

    if raton == gato:
        print("el Gato ha ganado")
        break

    # ── turno gato ───────────────────────────────────────────────
    mejor_val = float("inf")
    mejores = []
    for mov in posibles_movimientos(gato):
        val = minimax(raton, mov, PROFUNDIDAD, True)
        if val < mejor_val:
            mejor_val = val
            mejores = [mov]
        elif val == mejor_val:
            mejores.append(mov)
    # en la lista de mejores, elije la distancia mas corta
    gato = mejores[0]
    for mej in mejores:
        if distancia_manhattan(mov, raton) < distancia_manhattan(gato, raton):
            gato = mej

    print()
    print("mueve gato")
    imprimir_tablero(raton, gato)
    
    if raton == gato:
        print("el Gato ha ganado")
        break

    turno = turno + 1

if turno > MAX_TURNOS:
    print("gano el raton")