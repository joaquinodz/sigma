from constantes import ACIERTOS, INTENTOS, NOMBRE
from tablero import los_casilleros_son_iguales, cambiar_de_estado_al_casillero

jugadores = []
jugador_actual = 0

def procesar_resultados(posiciones):
    """
    Joaquin: Determina si el jugador encontó 2 fichas iguales y actualiza sus estadísticas según el caso.
    Devuelve el indice del jugador que le corresponde el siguiente turno
    """
    global jugador_actual
    
    # Estructura de el parámetro posiciones (tupla):
    primera_posicion, segunda_posicion = posiciones

    jugadores[jugador_actual][INTENTOS] += 1
    
    # Si las posiciones son iguales, se suma 1 al contador de aciertos del jugador actual
    if los_casilleros_son_iguales(primera_posicion, segunda_posicion):
        jugadores[jugador_actual][ACIERTOS] += 1    

    else:
        # Si no, se cambia el estado de la ficha de la 1° y 2° posición a "oculta"
        cambiar_de_estado_al_casillero(primera_posicion, False)
        cambiar_de_estado_al_casillero(segunda_posicion, False)

        # Es turno de otro jugador
        if jugador_actual < len(jugadores) - 1:
            jugador_actual += 1
        else:
            jugador_actual = 0

def nombre_jugador_actual():
    """Joaquin: Devuelve el nombre del jugador actual."""
    return jugadores[jugador_actual][NOMBRE]

def agregar_jugador(nombre_nuevo):
    """Fatima/Rodrigo: agrega un jugador a la lista de jugadores con sus variables inicializadas en 0."""
    jugadores.append([nombre_nuevo,0,0])


def obtener_nombres_de_jugadores():
    """
    Fátima: obtener todos los nombres de los jugadores
    """
    nombres = ""
    if jugadores:
        for jugador in jugadores: 
            nombres += jugador[NOMBRE] +"\n"
    return nombres


def obtener_promedio_de_intentos():
    """Felipe: Se calcula el promedio de intentos de los jugadores en la partida."""
    total_intentos = 0
    for jugador in jugadores:
        total_intentos += jugador[INTENTOS]

    return total_intentos / len(jugadores)

def calcula_ganador():
    """
    Felipe: Devuelve la lista de jugadores ordenada  segun sus aciertos,
            en caso de empatar segun sus intentos.
    """
    return sorted(jugadores, reverse=True, key=lambda jugador: (jugador[ACIERTOS], -jugador[INTENTOS]))