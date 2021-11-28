import time
  
from constantes import *
import interfaz
from tablero import inicializar_tablero, refresca_tablero, pedir_datos, finalizar
from jugador import procesar_resultados, mostrar_resultados
from util import limpiar_consola, tiempo_de_juego
from manejo_de_archivos import convertir_contrasenia_a_diccionario, cargar_configuracion

def memotest_juego():
    """
    Logica general del juego, loop principal
    Hecha por todo el grupo (cada uno implemento su funcion).
    """
    while not finalizar():
        print(f"Turno de {interfaz.jugadores[interfaz.jugador_actual][NOMBRE]}")
        refresca_tablero()

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_datos("1° Posición: ")

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_datos("2° Posición: ")
        
        procesar_resultados((primera_posicion, segunda_posicion))

        finalizar_turno()

def finalizar_turno():
    """
    Joaquin: Ejecuta las tareas necesarias para finalizar el turno
    """
    time.sleep(2)
    limpiar_consola()

def main():
    cargar_configuracion()
    return
    diccionario_usuarios_contrasenias = convertir_contrasenia_a_diccionario()
    interfaz.crear_interfaz(diccionario_usuarios_contrasenias)
    try:
        inicializar_tablero()
        inicio = time.time()

        memotest_juego()

        tiempo_de_juego(inicio)

        mostrar_resultados()
    except IndexError:
        print("La ventana de registro fue cerrada.\n")
    #permite que el usuario lea el resultado antes de que se cierre la ventana
    input("Pulse enter para finalizar\n\n")

main()
