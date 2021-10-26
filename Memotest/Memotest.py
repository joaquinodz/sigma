

def memotest_juego():

    tablero = [["s", False], ["D", False], ["s", False], ["D", False]] #Acá tengo acomodado el tablero con su posicion (indice, letra y estado del juego). 
    

    while not finalizar(tablero):
        posiciones= [[1],[2],[3],[4]]
        posiciones_provisorias = [[1],[2],[3],[4]]

        print("Fichas y posiciones: ", posiciones_provisorias)
        primera_posicion = int(input("1er. Posición: "))
        imagen_primera_posicion = tablero [primera_posicion -1][0] #en este caso obtengo la ubicación con su imagen
        tablero[primera_posicion-1][1] = True 
        posiciones_provisorias[primera_posicion -1]= imagen_primera_posicion

        print("Fichas y posiciones: ", posiciones_provisorias)
        segunda_posicion = int(input("2da. Posición: "))
        imagen_segunda_posicion = tablero [segunda_posicion -1][0] #en este caso obtengo la ubicación con su imagen
        tablero[segunda_posicion-1][1] = True
        posiciones_provisorias[segunda_posicion -1]= imagen_segunda_posicion
        
        print("Fichas y posiciones: ", posiciones_provisorias)

        if imagen_primera_posicion != imagen_segunda_posicion:

            posiciones_provisorias=posiciones
            tablero[primera_posicion-1][1] = False
            tablero[segunda_posicion-1][1] = False
        else:
            
            finalizar(tablero)
            
        print("Fichas y posiciones: ", posiciones_provisorias)
        tercera_posicion = int(input("1er. Posición: "))
        imagen_tercera_posicion = tablero [tercera_posicion -1][0] #en este caso obtengo la ubicación con su imagen
        tablero[tercera_posicion-1][1] = True 
        posiciones_provisorias[tercera_posicion -1]= imagen_tercera_posicion
        
        print("Fichas y posiciones: ", posiciones_provisorias)
        cuarta_posicion = int(input("2da. Posición: "))
        imagen_cuarta_posicion = tablero [cuarta_posicion -1][0] #en es1te caso obtengo la ubicación con su imagen
        tablero[cuarta_posicion-1][1] = True 
        posiciones_provisorias[cuarta_posicion -1]= imagen_cuarta_posicion
        print("Fichas y posiciones: ", posiciones_provisorias)

        if imagen_tercera_posicion == imagen_cuarta_posicion:

            finalizar(tablero)
        else:

            posiciones_provisorias= posiciones
            tablero[tercera_posicion-1][1] = False
            tablero[cuarta_posicion-1][1] = False
        
    return tablero

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
    memotest_juego()

main()
