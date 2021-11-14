import time

from util import limpiar_consola, tiempo_de_juego
from tablero import inicializar_tablero, refresca_tablero, pedir_datos, finalizar, IMAGEN_FICHA, ESTADO_FICHA, CANTIDAD_DE_FICHAS
from jugador import procesar_resultados, NOMBRE

def memotest_juego(tablero, jugadores):
    jugador_actual_id = 0

    while not finalizar(tablero):
        print(f"Turno de {jugadores[jugador_actual_id][NOMBRE]}")
        refresca_tablero(tablero)

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_datos("1° Posición: ", tablero)

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_datos("2° Posición: ", tablero)
        
        procesar_resultados(tablero, jugadores, jugador_actual_id, (primera_posicion, segunda_posicion))
        finalizar_turno(tablero)

        # Ahora es turno del otro jugador (TODO: mejorarlo un toque)
        jugador_actual_id = (1 - jugador_actual_id)

def finalizar_turno(tablero):
    """
    Joaquin: Ejecuta las tareas necesarias para finalizar el turno
    """
    time.sleep(2)
    limpiar_consola()

def main():
    """
    tablero es una lista cuyos elementos representan cada "casillero" de el tablero
    cada casillero tiene a su vez una lista con dos valores
    el primer valor representa la imagen que tiene el casillero
    y el segundo valor representa si esta descubierto o no.
    """
    jugadores = [["juan", 0, 0], ["manuel", 0, 0]]
    tablero = inicializar_tablero(CANTIDAD_DE_FICHAS)
    inicio = time.time()

    memotest_juego(tablero, jugadores)

    tiempo_de_juego(inicio)

main()
