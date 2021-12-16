import interfaz_partidas

from interfaz import crear_interfaz
from Memotest import jugar_memotest
from manejo_de_archivos import cargar_configuracion, convertir_contrasenia_a_diccionario, grabar_datos_de_la_partida

def main():
    configuracion = cargar_configuracion()
    
    #Interfaz de inicio.
    crear_interfaz(configuracion, convertir_contrasenia_a_diccionario())

    jugar_memotest(configuracion)
    

    interfaz_partidas.mostrar_ventana()

main()