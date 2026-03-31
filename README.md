# minimax

Un juego donde el gato persigue al raton y el raton intenta escapar del gato la mayor cantidad de turnos, si logra escapar por X turnos, gana el raton.
Ambos agentes se mueven en cuatro direcciones en un tablero de 6x6 sin obstaculos

## Que funciono, que fue un desastre y el mejor momento AJA!

Todo fue tomando forma desde el inicio, la creacion del tablero, la posicion inicial de los agentes y que uno persiga al otro.

Lo que fue un desastre fue mi intento de hacer que el juego sea balanceado en un tablero sin obstaculos, donde existe un concepto que se aleja del scope del programa, que es el argumento de paridad, lo cual define quien ganara el juego dependiendo de la propia distancia en la que se encuentran al inicio del juego.

El mejor momento del proceso fue descubrir que podia variar quien acababa ganando si colocaba a los agentes de forma aleatoria en el tablero.
