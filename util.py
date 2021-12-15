"""
    Acá van las funciones conceptualmente independientes al manejo del tablero y de la partida.
"""
import time
import os
import random

def calcular_tiempo_de_juego(inicio):
    """ Sandra: Muestra el  tiempo que ha tomado la partida."""
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    segundos_a_horas = tiempo_transcurrido / 3600
    segundos_a_minutos = tiempo_transcurrido / 60
    
    horas = round(segundos_a_horas)
    minutos = round(segundos_a_minutos) % 60
    segundos = round(tiempo_transcurrido % 60)

    return (horas, minutos, segundos)
   
def limpiar_consola():
    """Joaquin: Limpiamos la consola (compatible con Windows, Linix y Mac)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def castear_valor(valor):
    """Joaquin: Infiere el tipo de dato a partir de un string y realiza la conversion correspondiente a su tipo de dato primitivo"""
    valor_convertido = None

    """
    Para el casteo a booleano hago esto asi porque:
        bool('False') = True
        bool('True') = True
        bool('') = False
    """

    if valor.isnumeric():
        valor_convertido = int(valor)
    
    elif valor.lower() in ['true', 'True']:
        valor_convertido = True
    
    elif valor.lower() in ['false', 'False']:
        valor_convertido = False

    return valor_convertido

def mezclar_lista(lista):
    """Rodrigo: Mezcla la lista pasada por parametros."""
    random.shuffle(lista)