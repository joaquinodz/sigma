from tablero import IMAGEN_FICHA, ESTADO_FICHA

NOMBRE = 0
INTENTOS = 1
ACIERTOS = 2

def procesar_resultados(tablero, jugadores, jugador_id, posiciones):
    """
    Joaquin: Determina si el jugador encontó 2 fichas iguales y actualiza sus estadísticas según el caso.
    Devuelve True si acertó, False si no.
    """
    acerto = False

    # Estructura de el parámetro posiciones (tupla):
    primera_posicion, segunda_posicion = posiciones

    if tablero[primera_posicion][IMAGEN_FICHA] == tablero[segunda_posicion][IMAGEN_FICHA]:
        jugadores[jugador_id][ACIERTOS] += 1    
        acerto = True
    else:
        tablero[primera_posicion][ESTADO_FICHA] = False
        tablero[segunda_posicion][ESTADO_FICHA] = False
    
    jugadores[jugador_id][INTENTOS] += 1

    return acerto

def obtener_jugadores(raiz,jugador_uno,jugador_dos):
    INTENTOS = 0
    PUNTOS = 0
    """
    Rodrigo: obtiene los jugadores ingresados en la interfaz grafica, genera la lista de jugadores
    con sus puntos y sus intentos, la mezcla para ser almacenada en una variable global
    """
    global lista_jugadores
    lista_jugadores = [[jugador_uno.get(),INTENTOS,PUNTOS],[jugador_dos.get(),INTENTOS,PUNTOS]]
    random.shuffle(lista_jugadores)
    raiz.destroy()