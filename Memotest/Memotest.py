
diccionario = {1:"s" , 2:"D" , 3:"s" , 4:"D"}


def construccion_tablero(eleccion,tablero):
    tablero_actualizado = tablero
    tablero_actualizado[eleccion-1] = diccionario[eleccion]

    return tablero_actualizado





def memotest_juego(diccionario_fichas):
    contador = 0
    posiciones = diccionario_fichas.keys()
    posiciones = list(posiciones)
    posiciones_provisorias = posiciones
    
    

    while contador < 2 :
        print(posiciones)
        primer_ficha = int(input("Por favor, ingrese el numero de la primer ficha: "))
        posiciones_provisorias = construccion_tablero(primer_ficha, posiciones_provisorias)


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
        





    
def main():
    memotest_juego(diccionario)


main()
