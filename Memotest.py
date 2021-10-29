import time

IMAGEN_FICHA = 0
ESTADO_FICHA = 1
CANTIDAD_DE_FICHAS = 8
FICHAS_POR_FILA = 4

def memotest_juego(tablero):
    refresca_tablero(tablero)

    while not finalizar(tablero):

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_datos("1° Posición: ", tablero)

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_datos("2° Posición: ", tablero)

        if tablero[primera_posicion][IMAGEN_FICHA] != tablero[segunda_posicion][IMAGEN_FICHA]:
            tablero[primera_posicion][ESTADO_FICHA] = False
            tablero[segunda_posicion][ESTADO_FICHA] = False
            refresca_tablero(tablero)

def refresca_tablero(tablero):
    """ Felipe: esta funcion se encarga de printear por pantalla el tablero dado por parametro """
    os.system("clear")
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

    time.sleep(1)
    
    # TODO: Limpiar consola.
    
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

def inicializar_tablero(cantidad_de_fichas):
    """Joaquin: crea la estructura del tablero y decide el orden de las fichas"""
    tablero = []

    for i in range(cantidad_de_fichas):
        """
        POR AHORA:
            Meto las "s" en los casilleros impares y las "D" en los pares
            Parece que en la siguiente etapa vamos a tener que hacer un random
        """

        if i % 2 != 0:
            tablero.append(["s", False])

        else:
            tablero.append(["D", False])

    return tablero

def main():
    """
    tablero es una lista cuyos elementos representan cada "casillero" de el tablero
    cada casillero tiene a su vez una lista con dos valores
    el primer valor representa la imagen que tiene el casillero
    y el segundo valor representa si esta descubierto o no.
    """
    tablero = inicializar_tablero(CANTIDAD_DE_FICHAS)
    memotest_juego(tablero)

main()
