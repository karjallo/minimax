from funciones import posibles_movimientos, distancia_manhattan


# va a ser necesario realizar alguna funcion que permita evaluar las posiciones de ambos animales,
# por heuristica utilizariamos distancia manhattan | Xg - Xr | + | Yg - Yr |
def minimax(tablero, profundidad, es_maximizador):
# verificamos si se cumple alguna de las condiciones de victoria
# debo buscar los valores 1 y 2 correspondientes al gato y al raton en el tablero, 
# tal vez sea necesario eliminar mi funcion de ganador
# si se termino el juego?:
# si gano el gato dar -10
# si gano el raton dar +10

# aca realizar la evaluacion por posicion 

    # si es el turno del raton (maximizador)

    # Hallamos las posiciones del gato y del raton con el tablero
    for filas in tablero:
        for columna in filas:
            if columna == 1:
                pos_gato = [filas, columna]
            if columna == 2:
                pos_raton = [filas, columna]

    distancia = distancia_manhattan(pos_gato, pos_raton)

    if pos_gato == pos_raton:
        puntaje = -100
    elif profundidad == 20:
        puntaje = 100
    else:
        puntaje = distancia

    if es_maximizador:
        mejor_puntaje = float('-inf')
        movimientos = posibles_movimientos(pos_raton, len(tablero[0]), len(tablero))

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
        movimientos = posibles_movimientos(pos_gato, len(tablero[0]), len(tablero))

        for movimiento in movimientos:
            #simular movimiento
            #mover()
            puntaje = minimax(tablero, profundidad + 1, True)
            # deshacer_movimiento()
            mejor_puntaje = min(puntaje, mejor_puntaje)
        return mejor_puntaje