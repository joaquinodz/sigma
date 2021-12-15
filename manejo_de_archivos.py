import jugador

from constantes import CONFIGURACION_DEFAULT, CLAVE, VALOR, NOMBRE, ACIERTOS, INTENTOS
from util import smart_cast
from datetime import datetime

def cargar_configuracion():
    """Joaquin: Carga la configuración del juego desde un archivo"""

    with open("configuracion.csv", 'r') as archivo_configuracion:
        lista_de_lineas = archivo_configuracion.readlines()
    
    # Saco el salto de linea al final de cada linea
    # Convierto los valores separados por coma en listas - [clave, valor]
    lista_de_lineas = [linea.rstrip('\n').split(',') for linea in lista_de_lineas]
    
    # {'nombre_del_parametro': valor_del_parametro}
    configuracion = {linea[CLAVE]:smart_cast(linea[VALOR]) for linea in lista_de_lineas}

    # Si no hay configuracion, uso la configuracion por defecto
    for clave in CONFIGURACION_DEFAULT:
        if clave not in configuracion:
            configuracion[clave] = CONFIGURACION_DEFAULT[clave]
    
    return configuracion

def convertir_contrasenia_a_diccionario():
    """Rodrigo: convierte el archivo de contrasenias a un diccionario"""
    contrasenias = open("usuarios.csv","r")
    diccionario_contrasenias = {}
    linea = leer_linea(contrasenias)
    while linea:
        diccionario_contrasenias[linea[CLAVE]] = linea[VALOR]
        linea = leer_linea(contrasenias)
    contrasenias.close()
    
    return diccionario_contrasenias

def leer_linea(archivo):
    """
    Rodrigo: lee una linea proveniente de un arhivo especificado por parametro
    """
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        linea_procesada = linea.split(',')
    else:
        linea_procesada = None

    return linea_procesada

#----------------------------ESCRITURA----------------------------#
def escribir_archivo(archivo, linea):
    """
    Fátima: escribe linea pasada por parámetro al archivo
    """
    archivo.write(linea)

def registrar_jugadores_en_archivo(nuevos_jugadores_registrados):
    """
    Fátima: registro nuevos usuarios al archivo partir de la lista de jugadores nuevos.
    Como anteriormente ya fueron verificados, es seguro escribirlos directo en el archivo
    """
    usuarios = open("usuarios.csv" ,"a")


    if nuevos_jugadores_registrados:
        for usuario in nuevos_jugadores_registrados: 
            nuevo_usuario =  usuario[CLAVE] + "," + usuario[VALOR] + "\n"
            escribir_archivo(usuarios, nuevo_usuario)        

    usuarios.close()

def grabar_datos_de_la_partida():
    """
    Felipe: Graba los datos de los jugadores obtenidos por cada partida en el archivo partidas.csv
    """
    datos_de_la_partida = open("partidas.csv" ,"a")

    for usuario in jugador.jugadores:
        escribir_archivo(datos_de_la_partida, datetime.today().strftime("%Y/%m/%d") + "," + datetime.now().strftime("%H:%M:%S") + f",{usuario[NOMBRE]},{usuario[ACIERTOS]},{usuario[INTENTOS]}" + "\n")        

    datos_de_la_partida.close()
