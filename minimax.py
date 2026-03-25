from funciones import posibles_movimientos


# va a ser necesario realizar alguna funcion que permita evaluar las posiciones de ambos animales,
# por heuristica utilizariamos distancia manhattan | Xg - Xr | + | Yg - Yr |
def minimax(tablero, profundidad, es_maximizador):
 # verificamos si se cumple alguna de las condiciones de victoria
# debo buscar los valores 1 y 2 correspondientes al gato y al raton en el tablero, 
# tal vez sea necesario eliminar mi funcion de ganador
# si se termino el juego?:
# si gano el gato dar -10
# si gano el raton dar +10

   # si es el turno del raton (maximizador)
   if es_maximizador:
       mejor_puntaje = -infinity
       for posibilidad in posibles_movimientos:
           #simular movimiento
           #mover()
           puntaje = minimax(tablero, profundidad + 1, False)
           # deshacer_movimiento()
           mejor_puntaje = max(puntaje, mejor_puntaje)
       return mejor_puntaje

   # si es el turno del gato (minimizador)
   else:
       mejor_puntaje = +infinity
       for posibilidad in posibles_movimientos:
           #simular movimiento
           #mover()
           puntaje = minimax(tablero, profundidad + 1, True)
           # deshacer_movimiento()
           mejor_puntaje = min(puntaje, mejor_puntaje)
       return mejor_puntaje