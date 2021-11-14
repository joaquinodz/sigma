from tablero import IMAGEN_FICHA, ESTADO_FICHA

NOMBRE = 0
INTENTOS = 1
ACIERTOS = 2

def procesar_resultados(tablero, jugadores, jugador_id, posiciones):
    """
    Joaquin: Determina si el jugador encontó 2 fichas iguales y actualiza sus estadísticas según el caso.
    """
    
    # Estructura de el parámetro posiciones (tupla):
    primera_posicion, segunda_posicion = posiciones

    if tablero[primera_posicion][IMAGEN_FICHA] == tablero[segunda_posicion][IMAGEN_FICHA]:
        jugadores[jugador_id][ACIERTOS] += 1    
    else:
        tablero[primera_posicion][ESTADO_FICHA] = False
        tablero[segunda_posicion][ESTADO_FICHA] = False
    
    jugadores[jugador_id][INTENTOS] += 1