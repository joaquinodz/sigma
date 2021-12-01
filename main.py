import interfaz
import constantes
import manejo_de_archivos
from manejo_de_archivos import convertir_contrasenia_a_diccionario, cargar_configuracion
import Memotest

def main():
    constantes.configuracion = cargar_configuracion()
    
    diccionario_usuarios_contrasenias = convertir_contrasenia_a_diccionario()
    interfaz.crear_interfaz(diccionario_usuarios_contrasenias)
    Memotest.funcion_englobadora_de_funciones()
    
    

main()
