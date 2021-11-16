import time

from util import limpiar_consola, tiempo_de_juego
from tablero import inicializar_tablero, refresca_tablero, pedir_datos, finalizar, IMAGEN_FICHA, ESTADO_FICHA, CANTIDAD_DE_FICHAS

def memotest_juego(tablero):
    refresca_tablero(tablero)
    intento = 0

    while not finalizar(tablero):

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_datos("1° Posición: ", tablero)

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_datos("2° Posición: ", tablero)
        
        finaliza_turno(tablero, intento, primera_posicion, segunda_posicion)

    print(f"Intentos realizados: {intento}")

def finaliza_turno(tablero, intento, primera_posicion, segunda_posicion):
    """
    Joaquin: Esta funcion es la que se encarga de verificar si las fichas son iguales
    """
    time.sleep(2)
    limpiar_consola()

    if tablero[primera_posicion][IMAGEN_FICHA] != tablero[segunda_posicion][IMAGEN_FICHA]:
        tablero[primera_posicion][ESTADO_FICHA] = False
        tablero[segunda_posicion][ESTADO_FICHA] = False

    refresca_tablero(tablero)
    intento += 1

def finaliza_juego(jugadores):
    """
    Felipe: Calcula el ganador y lo muestra por pantalla junto con los puntos de cada jugador.
    """
    ganador = -1
    msj_resultados = ""

    msj_resultados += f"\n {jugadores[0][NOMBRE_JUGADOR]}: {jugadores[0][PUNTOS_JUGADOR]} pts. \n"
    msj_resultados += f"{jugadores[1][NOMBRE_JUGADOR]}: {jugadores[1][PUNTOS_JUGADOR]} pts. \n"

    if jugadores[0][PUNTOS_JUGADOR] > jugadores[1][PUNTOS_JUGADOR]:
        ganador = 0
    elif jugadores[1][PUNTOS_JUGADOR] > jugadores[0][PUNTOS_JUGADOR]:
        ganador = 1
    else:
        if jugadores[0][TURNOS_JUGADOR] > jugadores[1][TURNOS_JUGADOR]:
            ganador = 1
        else:
            ganador = 0

    msj_resultados += f"\n Ganador: {jugadores[ganador][NOMBRE_JUGADOR]}"
    msj_resultados += ", por menor cantidad de turnos \n" if jugadores[0][PUNTOS_JUGADOR] == jugadores[1][PUNTOS_JUGADOR] else "\n"

    print(msj_resultados)

def main():
    """
    tablero es una lista cuyos elementos representan cada "casillero" de el tablero
    cada casillero tiene a su vez una lista con dos valores
    el primer valor representa la imagen que tiene el casillero
    y el segundo valor representa si esta descubierto o no.
    """
 
    tablero = inicializar_tablero(CANTIDAD_DE_FICHAS)
    inicio = time.time()
    memotest_juego(tablero)
    tiempo_de_juego(inicio)
    finaliza_juego(jugadores)

main()
