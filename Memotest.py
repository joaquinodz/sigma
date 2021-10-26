

def memotest_juego():

    tablero = [["s", False], ["D", False], ["s", False], ["D", False]] # Acá tengo acomodado el tablero con su posicion (indice, letra y estado del juego). 
    posiciones = [[1],[2],[3],[4]]
    posiciones_provisorias = [[1],[2],[3],[4]]

    while not finalizar(tablero):
        
        try:
        
            print("Fichas y posiciones: ", posiciones_provisorias)
            primera_posicion = int(input("1er. Posición: "))
            imagen_primera_posicion = tablero[primera_posicion - 1][0] # en este caso obtengo la ubicación con su imagen
            tablero[primera_posicion - 1][1] = True 
            posiciones_provisorias[primera_posicion - 1] = imagen_primera_posicion

            print("Fichas y posiciones: ", posiciones_provisorias)
            segunda_posicion = int(input("2da. Posición: "))
            imagen_segunda_posicion = tablero [segunda_posicion - 1][0] # en este caso obtengo la ubicación con su imagen
            tablero[segunda_posicion - 1][1] = True
            posiciones_provisorias[segunda_posicion - 1]= imagen_segunda_posicion
                
            print("Fichas y posiciones: ", posiciones_provisorias)

            if imagen_primera_posicion != imagen_segunda_posicion:
                posiciones_provisorias = posiciones
                tablero[primera_posicion - 1][1] = False
                tablero[segunda_posicion - 1][1] = False
            else:
                posiciones = posiciones_provisorias
        
        except ValueError:
            print("Has ingresado un número inválido. Intente nuevamente...")

        except IndexError:
            print(f"Debes ingresar un número entre 0 y {len(tablero)}")
                
            
            
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
    """ rodrigo: chequea que todos los valores del tablero sean True, si lo son devuelve True, si no, devuelve False """
    devolver = True
    
    for elemento in tablero:
        if not elemento[1]:
            devolver = False
            
    return devolver

    
def main():
    memotest_juego()

main()
