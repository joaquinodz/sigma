import interfaz_partidas

from interfaz import crear_interfaz
from Memotest import jugar_memotest
from manejo_de_archivos import cargar_configuracion, convertir_contrasenia_a_diccionario, registrar_jugadores_en_archivo, grabar_datos_de_la_partida

def main():
    configuracion = cargar_configuracion()

    #Interfaz de inicio.
    crear_interfaz(configuracion, convertir_contrasenia_a_diccionario())

    #inicio = time.time()
    jugar_memotest(configuracion)
    
    grabar_datos_de_la_partida()
    #registrar_jugadores_en_archivo()

    interfaz_partidas.mostrar_ventana()

main()