"""
    Acá van las funciones conceptualmente independientes al manejo del tablero y de la partida.
"""
import time
import os

def mostrar_tiempo_de_juego(inicio):
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

def smart_cast(value):
    """Joaquin: Infiere el tipo de dato a partir de un string y realiza la conversion correspondiente"""
    if value.isnumeric():
        return int(value)
    
    if "True" in value or "False" in value:
        return bool(value)
    
    return value