import random

IMAGEN_FICHA = 0
ESTADO_FICHA = 1
CANTIDAD_DE_FICHAS = 16
FICHAS_POR_FILA = 4

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

def refresca_tablero(tablero):
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

def pedir_datos(mensaje, tablero):
    """
    Joaquin: Le pide las posiciones al usuario las veces que sea necesario hasta que ingrese datos válidos
    Devuelve un entero con la posición que introdujo el usuario
    """
    pedir = True
    valor = 0

    while (pedir):
        try:
            valor = int(input(mensaje)) - 1

            if valor < 0 or valor > len(tablero) - 1:
                print(f"Debes ingresar un número entre 1 y {len(tablero)}")

            elif tablero[valor][ESTADO_FICHA]:
                print("Esa posición ya se encuentra visible. Elige otra...")

            else:
                pedir = False

        except ValueError:
            print("Has ingresado un número inválido. Intente nuevamente...")

    tablero[valor][ESTADO_FICHA] = True
    refresca_tablero(tablero)

    return valor

def finalizar(tablero):
    """ rodrigo: chequea que todos los valores del tablero sean True, si lo son devuelve True, si no, devuelve False """
    estado_tablero = True
    casillero = 0

    while estado_tablero and casillero < len(tablero):
        if not tablero[casillero][ESTADO_FICHA]:
            estado_tablero = False
        else:
            casillero +=1

    return estado_tablero