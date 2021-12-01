import time
  
import constantes

import interfaz
import tablero

from tablero import inicializar_tablero, refresca_tablero, pedir_posicion, finalizar, reinicio_tablero
from jugador import procesar_resultados, mostrar_resultados
from util import limpiar_consola, mostrar_tiempo_de_juego
from manejo_de_archivos import convertir_contrasenia_a_diccionario, cargar_configuracion

def memotest_juego():
    """
    Logica general del juego, loop principal
    Hecha por todo el grupo (cada uno implemento su funcion).
    """
    jugador_actual = 0

    while not finalizar():
        print(f"Turno de {interfaz.jugadores[interfaz.jugador_actual][constantes.NOMBRE]}")
        refresca_tablero()

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_posicion("1° Posición: ")

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_posicion("2° Posición: ")
        
        procesar_resultados(jugador_actual, (primera_posicion, segunda_posicion))

        finalizar_turno()

def finalizar_turno():
    """
    Joaquin: Ejecuta las tareas necesarias para finalizar el turno
    """
    time.sleep(2)
    limpiar_consola()

def funcion_englobadora_de_funciones():
    """Rodrigo: esta funcion engloba las funciones principales del programa"""
    
    try:
        inicializar_tablero()
        
        inicio = time.time()

        memotest_juego()

        mostrar_tiempo_de_juego(inicio)

        interfaz.pantalla_final()
            
    except IndexError:
        print("La ventana de registro fue cerrada.\n")


