def memotest_juego(diccionario_fichas):
    imagenes = ("s", "D")
    tablero = [[0, False], [1, False], [0, False], [1, False]]
    contador = 0
    posiciones = diccionario_fichas.keys()
    posiciones = list(posiciones)
    posiciones_provisorias = posiciones

    while contador < 2:
        print(posiciones)
        primer_ficha = int(input("Por favor, ingrese el numero de la primer ficha: "))
        posiciones_provisorias = construccion_tablero(primer_ficha, posiciones_provisorias)

        tablero[posicion-1][1] = True

        #aca se da el problema, por alguna razon, "posiciones" tiene el mismo valor que "posiciones_provisorias"

        print(posiciones_provisorias)
        segunda_ficha = int(input("Por favor, ingrese el numero de la segunda ficha: "))
        posiciones_provisorias = construccion_tablero(segunda_ficha , posiciones_provisorias)
        print(posiciones_provisorias)

        if diccionario[primer_ficha] == diccionario[segunda_ficha]:
            contador += 1
            posiciones = posiciones_provisorias
        else:
            posiciones_provisorias = posiciones

def refresca_tablero(tablero, imagenes):
    """ Felipe: esta funcion se encarga de printear por pantalla el tablero dado por parametro """
    tablero_string = "Fichas y Posiciones: "
    casillero_posicion = 0

    for casillero in tablero:
        casillero_posicion += 1

        if casillero_posicion % 4 == 1 and casillero_posicion != 1:
            tablero_string += "/n"

        if casillero[1]:
            tablero_string += " " + imagenes[casillero[0]] + " "
        else:
            tablero_string += f" [{casillero_posicion}] "

def finalizar(tablero):
    devolver = True
    for elemento in tablero:
        if not elemento[1]:
            devolver = False
    return devolver

    
def main():
    memotest_juego(diccionario)

main()
