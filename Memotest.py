def memotest_juego():
    """
    tablero es una lista cuyos elementos representan cada "casillero" de el tablero
    cada casillero tiene a su vez una lista con dos valores
    el primer valor representa la imagen que tiene el casillero
    y el segundo valor representa si esta descubierto o no.
    """
    tablero = [["s", False], ["D", False], ["s", False], ["D", False]]
    descubiertos = []

    while not finalizar(tablero):
        try:
            refresca_tablero(tablero)
            primera_posicion = int(input("1er. Posición: ")) - 1
            tablero[primera_posicion][1] = True

            refresca_tablero(tablero)
            segunda_posicion = int(input("2da. Posición: ")) - 1

            if tablero[segunda_posicion][1] == False:
                if tablero[primera_posicion][0] == tablero[segunda_posicion][0]:
                    tablero[primera_posicion][1] = True
                    tablero[segunda_posicion][1] = True
                    
                else:
                    tablero[primera_posicion][1] = False

                refresca_tablero(tablero)

            else:
                print("Esa posición ya se encuentra visible. Elige otra...")

        except ValueError:
            print("Has ingresado un número inválido. Intente nuevamente...")

        except IndexError:
            print(f"Debes ingresar un número entre 1 y {len(tablero)}")


def refresca_tablero(tablero):
    """ Felipe: esta funcion se encarga de printear por pantalla el tablero dado por parametro """
    tablero_string = "Fichas y Posiciones: "
    casillero_posicion = 0

    for casillero in tablero:
        casillero_posicion += 1

        if casillero_posicion % 4 == 1 and casillero_posicion != 1:
            tablero_string += "/n"

        if casillero[1]:
            tablero_string += "  " + casillero[0] + "  "
        else:
            tablero_string += f" [{casillero_posicion}] "

    print(tablero_string)

def finalizar(tablero):
    """ rodrigo: chequea que todos los valores del tablero sean True, si lo son devuelve True, si no, devuelve False """
    devolver = True

    for elemento in tablero:
        if not elemento[1]:
            devolver = False

    return devolver


def main():
    memotest_juego()

main()
