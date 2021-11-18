import time
  
from constantes import *
import interfaz
from tablero import inicializar_tablero, refresca_tablero, pedir_datos, finalizar
from jugador import procesar_resultados, mostrar_resultados
from util import limpiar_consola, tiempo_de_juego

def memotest_juego():
    """
    Logica general del juego, loop principal
    Hecha por todo el grupo (cada uno implemento su funcion).
    """
    jugador_actual_id = 0

    while not finalizar():
        print(f"Turno de {interfaz.jugadores[jugador_actual_id][NOMBRE]}")
        refresca_tablero()

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_datos("1° Posición: ")

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_datos("2° Posición: ")
        
        if not procesar_resultados(jugador_actual_id, (primera_posicion, segunda_posicion)):
            # Ahora es turno del otro jugador
            jugador_actual_id = (1 - jugador_actual_id)

        finalizar_turno()

def finalizar_turno():
    """
    Joaquin: Ejecuta las tareas necesarias para finalizar el turno
    """
    time.sleep(2)
    limpiar_consola()

def main():
    interfaz.crear_interfaz()
    inicializar_tablero()
    inicio = time.time()

    memotest_juego()

    tiempo_de_juego(inicio)

    mostrar_resultados()
    #la variable finalizar permite que el usuario lea el resultado antes de que se cierre la ventana
    variable_finalizar = input("Pulse enter para finalizar")

main()
