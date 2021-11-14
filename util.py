import random
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


def inicializar_tablero(cantidad_de_fichas):
    """
    Inicializar tablero genera un tablero aleatoriamente a través de random.
    Comienza escogiendo una ficha al azar de la lista de fichas.
    Lo apendea a la lista del tablero que va a devolver, junto con el estado "False" que se va a utilizar en el juego.
    Al agregarlo a la lista lo remueve de las fichas posibles.
    Al final, al tablero se le hace un shuffle para mezclar el tablero.
    Rodrigo, Fátima.
    """
    cantidad_de_pares = cantidad_de_fichas / 2
    fichas = ['S', 'I', 'G', 'M', 'A', 'X', 'Y', 'Z', 'W', 'O', 's', 'Q', 'R', 'U', 't', 'p']
    tablero = []
    i = 1
    
    while i <= cantidad_de_pares:
        ficha_random = random.choice(fichas)
        tablero.append([ficha_random, False])
        tablero.append([ficha_random, False])
        fichas.remove(ficha_random)
        i += 1
    
    random.shuffle(tablero)

    return tablero