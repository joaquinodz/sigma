IMAGEN_FICHA = 0
ESTADO_FICHA = 1
CANTIDAD_DE_FICHAS = 16
FICHAS_POR_FILA = 4

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