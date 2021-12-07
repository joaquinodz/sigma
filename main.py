from manejo_de_archivos import cargar_configuracion
from interfaz import crear_interfaz, pantalla_final
from Memotest import logica_principal
from manejo_de_archivos import convertir_contrasenia_a_diccionario, registrar_jugadores_en_archivo

def main():
    configuracion = cargar_configuracion()

    #Interfaz de inicio.
    crear_interfaz(configuracion, convertir_contrasenia_a_diccionario())

    #inicio = time.time()
    cantidad_de_partidas_jugadas = 1
    logica_principal(configuracion)

    #Interfaz final.
    #mostrar_tiempo_de_juego(inicio)
    pantalla_final(configuracion, cantidad_de_partidas_jugadas)
    
    registrar_jugadores_en_archivo()

main()