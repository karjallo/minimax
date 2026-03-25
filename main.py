from re import randint
from funciones import presentacion, configuracion, crear_tablero, imprimir_juego, estado_juego, minimax, game_over
from minimax import minimax



# declaramos variables iniciales
turno = 1
# declaro una variable llamada repeticion para analizar casos infinitos
repeticion = 0
# definimos el turno raton, que solo se aumenta cuando el raton juega
# para definir su condicion de victoria
turno_raton = 0

# presentamos el juego
presentacion()
# realizamos las configuraciones necesarias para empezar el juego
parametros = configuracion()
dimension_x = parametros[0]
dimension_y = parametros[1]
jugador = parametros[2]
turno_win_raton = parametros[3]
profundidad = parametros[4]

# necesitamos crear un tablero, con las dimensiones definidas del usuario
tablero = crear_tablero(dimension_x, dimension_y)

# es posible que sea necesario declarar la antigua posicion del gato/raton
# para poder desdibujar en el juego, las posiciones serian random, en lo posible
# con algunas restricciones para evitar que el juego acabe muy rapido
posicion_gato = [randint(dimension_x), randint(dimension_y)]
posicion_raton = [randint(dimension_x), randint(dimension_y)]

# realizamos una comprobacion para verificar que no tengan la misma posicion al iniciar, si esto se cumple, ejecutaremos hasta conseguir una posicion diferente
# mas tarde podemos agregar otras opciones como, una distancia minima para que el valor sea aceptable
while posicion_raton == posicion_gato:
    posicion_raton = [randint(dimension_x), randint(dimension_y)]

# inicializamos estas variables, que representan la posicion anterior del gato y raton
# que utilizaremos mas adelante para facilitar la impresion del tablero y por si querramos definir
# algun empate o condicion de ganar en cuando cumplan x movimientos iguales, como en ajedrez
prepos_gato = posicion_gato
prepos_raton = posicion_raton


# necesitamos hacer algun tipo de loop, para que los movimientos vayan variando
# de pc a jugador, el mismo debe acabar cuando se considere que uno de los dos gano


# antes del loop, imprimir el juego con las posiciones iniciales
# posteriormente se imprimira al finalizar el turno de cada jugador
imprimir_juego(tablero)
#LOOP
# Aca debe de ejecutarse el algoritmo minmax, intercalando turnos, realizando una verificacion
# para comprobar el estado del juego
while estado_juego(posicion_gato, posicion_raton, turno_raton, turno_win_raton) == 0:
    # debe haber condicionales para saber si es el turno del jugador o de la pc y si
    # es del gato o del raton e caso de como debe correr, siendo min o max
    # puedo implementar algun tipo de contador para variar los turnos
    if turno % 2 > 0:
        # turno 1 siempre sera para raton
        turno_raton = turno_raton + 1
        mejor_movimiento = minimax(tablero, profundidad, True)
        mover(mejor_movimiento, posicion_raton)
        turno = turno + 1
        imprimir_juego(tablero)
    else:
        # turno 2 y turnos pares sera turno del gato
        mejor_movimiento = minimax(tablero, profundidad, False)
        turno = turno + 1

        imprimir_juego(tablero)

# realizamos la comprobacion de quien gano, y creamos la variable ganador para posteriormente poder imprimir el mensaje final
if estado_juego() == 1:
    ganador = "g"
elif estado_juego() == 2:
    ganador = "r"
# solo debug
else:
    print("por alguna razon, saltamos el bucle del juego sin tener un ganador")

# luego de definir que el juego concluyo se debe de presentar el ganador
# segun las funciones, el gato gana si las posiciones son iguales
# el raton gana si pasan 35 turnos ( debo modificar para que un turno pase tras 2 movimientos )
game_over(ganador, jugador)

