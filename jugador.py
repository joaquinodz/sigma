from constantes import IMAGEN_FICHA, ACIERTOS, ESTADO_FICHA, INTENTOS, NOMBRE
from tablero import tablero
import interfaz

def procesar_resultados(jugador_id, posiciones):
    """
    Joaquin: Determina si el jugador encontó 2 fichas iguales y actualiza sus estadísticas según el caso.
    Devuelve True si acertó, False si no.
    """
    acerto = False

    # Estructura de el parámetro posiciones (tupla):
    primera_posicion, segunda_posicion = posiciones

    if tablero[primera_posicion][IMAGEN_FICHA] == tablero[segunda_posicion][IMAGEN_FICHA]:
        interfaz.jugadores[jugador_id][ACIERTOS] += 1    
        acerto = True
    else:
        tablero[primera_posicion][ESTADO_FICHA] = False
        tablero[segunda_posicion][ESTADO_FICHA] = False
    
    interfaz.jugadores[jugador_id][INTENTOS] += 1

    return acerto

def mostrar_resultados():
    """
    Felipe: Calcula el ganador y lo muestra por pantalla junto con los puntos de cada jugador.
    """
    ganador = -1
    msj_resultados = ""

    msj_resultados += f"\n {interfaz.jugadores[0][NOMBRE]}: {interfaz.jugadores[0][ACIERTOS]} pts., Intentos: {interfaz.jugadores[0][INTENTOS]} \n"
    msj_resultados += f"{interfaz.jugadores[1][NOMBRE]}: {interfaz.jugadores[1][ACIERTOS]} pts., Intentos: {interfaz.jugadores[1][INTENTOS]} \n"

    if interfaz.jugadores[0][ACIERTOS] > interfaz.jugadores[1][ACIERTOS]:
        ganador = 0
    elif interfaz.jugadores[1][ACIERTOS] > interfaz.jugadores[0][ACIERTOS]:
        ganador = 1
    else:
        if interfaz.jugadores[0][INTENTOS] > interfaz.jugadores[1][INTENTOS]:
            ganador = 1
        else:
            ganador = 0

    msj_resultados += f"\n Ganador: {interfaz.jugadores[ganador][NOMBRE]}"
    msj_resultados += ", por menor cantidad de intentos \n" if interfaz.jugadores[0][ACIERTOS] == interfaz.jugadores[1][ACIERTOS] else "\n"

    print(msj_resultados)