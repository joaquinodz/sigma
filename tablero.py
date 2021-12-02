import random
import constantes
from constantes import IMAGEN_FICHA, ESTADO_FICHA, FICHAS_POR_FILA

"""
tablero es una lista cuyos elementos representan cada "casillero" de el tablero
cada casillero tiene a su vez una lista con dos valores
el primer valor representa la imagen que tiene el casillero
y el segundo valor representa si esta descubierto o no.
"""
tablero = []

def inicializar_tablero():
    """
    Inicializar tablero genera un tablero aleatoriamente a través de random.
    Comienza escogiendo una ficha al azar de la lista de fichas.
    Lo apendea a la lista del tablero que va a devolver, junto con el estado "False" que se va a utilizar en el juego.
    Al agregarlo a la lista lo remueve de las fichas posibles.
    Al final, al tablero se le hace un shuffle para mezclar el tablero.
    Rodrigo, Fátima.
    """
    
    cantidad_de_pares_de_fichas_totales = constantes.configuracion["CANTIDAD_FICHAS"] / 2
    fichas = ['S', 'I', 'G', 'M', 'A', 'X', 'Y', 'Z', 'W', 'O', 'Q', 'R', 'U', 't', 'p','a','b','c','d','f','r','j','F','s']
    cantidad_de_fichas_inicializadas = 1
    
    while cantidad_de_fichas_inicializadas <= cantidad_de_pares_de_fichas_totales:
        ficha_random = random.choice(fichas)
        tablero.append([ficha_random, False])
        tablero.append([ficha_random, False])
        fichas.remove(ficha_random)
        cantidad_de_fichas_inicializadas += 1
    
    random.shuffle(tablero)

def refresca_tablero():
    """ Felipe: esta funcion se encarga de printear por pantalla el tablero dado por parametro """
    
    tablero_string = "Fichas y Posiciones: \n"
    casillero_posicion = 0

    for casillero in tablero:
        casillero_posicion += 1

        if casillero_posicion % FICHAS_POR_FILA == 1 and casillero_posicion != 1:
            tablero_string += "\n"

        if casillero[ESTADO_FICHA]:
            tablero_string += "  " + casillero[IMAGEN_FICHA] + "  "
        else:
            tablero_string += f" [{casillero_posicion}] "
    
    print(tablero_string)

def pedir_posicion(mensaje):
    """
    Joaquin: Le pide las posiciones al usuario las veces que sea necesario hasta que ingrese datos válidos
    Devuelve un entero con la posición que introdujo el usuario
    """
    seguir_pidiendo_posicion = True
    valor = 0

    while seguir_pidiendo_posicion:
        try:
            valor = int(input(mensaje)) - 1

            if valor < 0 or valor > len(tablero) - 1:
                print(f"Debes ingresar un número entre 1 y {len(tablero)}")

            elif tablero[valor][ESTADO_FICHA]:
                print("Esa posición ya se encuentra visible. Elige otra...")

            else:
                seguir_pidiendo_posicion = False

        except ValueError:
            print("Has ingresado un número inválido. Intente nuevamente...")

    tablero[valor][ESTADO_FICHA] = True
    refresca_tablero()

    return valor

def juego_finalizado():
    """ rodrigo: chequea que todos los valores del tablero sean True, si lo son devuelve True, si no, devuelve False """
    estado_tablero = True
    casillero = 0

    while estado_tablero and casillero < len(tablero):
        if not tablero[casillero][ESTADO_FICHA]:
            estado_tablero = False
        else:
            casillero +=1

    return estado_tablero

def reiniciar_tablero():
    """Esta funcion reinicia el tablero a su estado original, dejandolo listo para jugar una nueva partida"""
    global tablero
    tablero = []