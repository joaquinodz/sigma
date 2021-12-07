import time

from tablero import inicializar_tablero, juego_finalizado, refresca_tablero, pedir_posicion
from jugador import nombre_jugador_actual, procesar_resultados
from util import limpiar_consola

def logica_principal(configuracion):
    """
    Esta funcion engloba las funciones principales del programa
    Hecha por todo el grupo (cada uno implemento su funcion)
    """

    try:
        #Inicializa variables.
        inicializar_tablero(configuracion)

        #Loop principal del juego.
        memotest_juego()
            
    except IndexError:
        print("La ventana de registro fue cerrada.\n")

def memotest_juego():
    """
    Logica general del juego, loop principal
    Hecha por todo el grupo (cada uno implemento su funcion).
    """

    while not juego_finalizado():
        print(f"Turno de {nombre_jugador_actual()}")
        refresca_tablero()

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_posicion("1° Posición: ")

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_posicion("2° Posición: ")
        
        procesar_resultados((primera_posicion, segunda_posicion))

        finalizar_turno()

def finalizar_turno():
    """
    Joaquin: Ejecuta las tareas necesarias para finalizar el turno
    """
    time.sleep(2)
    limpiar_consola()