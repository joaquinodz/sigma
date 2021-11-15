"""
    Acá van las funciones conceptualmente independientes al manejo del tablero y de la partida.
"""

import time
import os

def tiempo_de_juego(inicio):
    """ Sandra: Muestra el  tiempo que ha tomado la partida."""
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    segundos_a_horas = tiempo_transcurrido / 3600
    segundos_a_minutos = tiempo_transcurrido / 60
    
    horas = round(segundos_a_horas)
    minutos = round(segundos_a_minutos) % 60
    segundos = round(tiempo_transcurrido % 60)

    print(f"Tiempo de juego = horas: {horas}  minutos: {minutos}  segundos: {segundos}")
   
def limpiar_consola():
    """Joaquin: Limpiamos la consola (compatible con Windows, Linix y Mac)"""
    os.system('cls' if os.name == 'nt' else 'clear')