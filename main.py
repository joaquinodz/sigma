from manejo_de_archivos import cargar_configuracion
from interfaz import crear_interfaz
from Memotest import jugar_memotest
from manejo_de_archivos import convertir_contrasenia_a_diccionario, registrar_jugadores_en_archivo

def main():
    configuracion = cargar_configuracion()

    #Interfaz de inicio.
    crear_interfaz(configuracion, convertir_contrasenia_a_diccionario())

    jugar_memotest(configuracion)
    
    registrar_jugadores_en_archivo()

main()