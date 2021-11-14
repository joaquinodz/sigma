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

main()
