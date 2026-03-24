# se define el mensaje inicial
def presentacion():
    print('''
    Te despiertas en medio de un extraño laboratorio subterráneo. Las paredes están cubiertas de códigos garabateados, pantallas parpadeantes y… queso. Mucho queso. Frente a ti,
    una científica misteriosa —que claramente se parece a la versión cyborg de Marie Curie— dice con voz robótica:

    "Solo uno sobrevivirá en este laberinto de decisiones. ¿El astuto therian ratón?
    ¿O el implacable therian gato? Tú, aprendiz de estratega, tienes que decidir cómo se juega esta historia."
    ''')

# solicitamos la configuracion del usuario, realizar comprobaciones de que los datos sean correctos
# sera necesario mas adelante crear restricciones de las dimensiones del tablero
def configuracion():
    dimension_x = int(input("Cual es la dimension en X del laberinto?"))
    dimension_y = int(input("Cual es la dimension en Y del laberinto?"))
    jugador = " "
    while jugador != "g" or jugador != "r":
        jugador = input("Quien sos? Para Therian Gato escribe G, para Therian Raton escribe R").lower()
    turno_raton_win = int(input("Cuantos turnos tiene el raton para que pueda ganar?"))
    
    return [dimension_x, dimension_y, jugador, turno_raton_win]

def crear_tablero(dimension_x, dimension_y):
    tablero = []
    for y in range(dimension_y):
        # inicializamos / vaciamos la nueva fila
        fila = []
        # iteramos sobre cada columna de cada fila, seria elemento por elemento de la fila
        for x in range(dimension_x):
            fila.append(0)
        # tras crear la fila, agregamos al tablero la fila entera
        tablero.append(fila)
    
    return tablero

# comprobar que el juego haya terminado, si gano el gato, return 1, si gano el raton return 2
# en caso de que nadie haya ganado return 0
def estado_juego(pos_gato, pos_raton, turno_raton, turno_win_raton):
    if pos_gato == pos_raton:
        return 1
    elif turno_raton >= turno_win_raton:
        return 2
    
    return 0
    

# en caso de que el juego se haya terminado, mostrar el ganador
def game_over(ganador, jugador):
    # en caso de que el jugador haya ganado
    if jugador == ganador:
        print("Ganaste!")
        if ganador == "g":
            print("Devoraste al therian raton")
        else:
            print("Has logrado huir del therian gato")

    # en caso de que hayas perdido
    else:
        print("Perdiste!")
        if ganador == "g":
            print("Has sido devorado por un therian gato")
        else:
            print("El therian raton logro escapar")

# generar la funcion que hace print en terminal del estado del juego
def imprimir_juego(tablero):
    for filas in tablero:

        for columna in filas:
            # utilizamos el parametro end, para evitar que se imprima una nueva linea por cada print
            if columna == 0:
                print("|  ", end=" ")
            elif columna == 1:
                print("| G", end=" ")
            else:
                print("| R", end=" ")
        # utilizamos un print solo para imprimir una nueva linea y las ultimas paredes al terminar cada fila
        print("|")


