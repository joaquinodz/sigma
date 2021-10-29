def analizar_resultados(tablero, primera_posicion, segunda_posicion):
    if tablero[primera_posicion][0] == tablero[segunda_posicion][0]:
        tablero[primera_posicion][1] = True
        tablero[segunda_posicion][1] = True
        
    else:
        tablero[primera_posicion][1] = False

def pedir_datos(mensaje, tablero, numero_posicion):
    """
    Joaquin: Le pide las posiciones al usuario las veces que sea necesario hasta que ingrese datos válidos
             Devuelve un entero con la posición que introdujo el usuario
    """
    pedir = True
    valor = 0
    
    while (pedir):
        try:
            valor = int(input(mensaje)) - 1
            
            if valor < 0 or valor > len(tablero):
                raise IndexError
            
            if numero_posicion == 2 and tablero[valor][1] == True:
                print("Esa posición ya se encuentra visible. Elige otra...")
            
            return valor
        except ValueError:
            print("Has ingresado un número inválido. Intente nuevamente...")
        
        except IndexError:
            print(f"Debes ingresar un número entre 1 y {len(tablero)}")


def memotest_juego():
    """
    tablero es una lista cuyos elementos representan cada "casillero" de el tablero
    cada casillero tiene a su vez una lista con dos valores
    el primer valor representa la imagen que tiene el casillero
    y el segundo valor representa si esta descubierto o no.
    """
    tablero = [["s", False], ["D", False], ["s", False], ["D", False]]
    
    while not finalizar(tablero):
        refresca_tablero(tablero)
        
        # Solicitamos al usuario la 1° posicion y validamos el valor
        primera_posicion = pedir_datos("1° Posición: ", tablero, 1)

        # Mostramos que tiene esa posición
        tablero[primera_posicion][1] = True
        refresca_tablero(tablero)

        # Solicitamos al usuario la 2° posicion y validamos el valor    
        segunda_posicion = pedir_datos("2° Posición: ", tablero, 1)

        analizar_resultados(tablero, primera_posicion, segunda_posicion)
            
        refresca_tablero(tablero)

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
