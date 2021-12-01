import constantes
from constantes import USUARIO,CONTRASENIA, CONFIGURACION_DEFAULT

def leer_archivo(archivo):
    """
    Rodrigo: lee un archivo linea a linea
    """
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        linea_procesada = linea.split(',')
    else:
        linea_procesada = None

    return linea_procesada

def convertir_contrasenia_a_diccionario():
    """Rodrigo: convierte el archivo de contrasenias a un diccionario"""
    contrasenias = open("usuarios.csv","r")
    diccionario_contrasenias = {}
    linea = leer_archivo(contrasenias)
    while linea[USUARIO]:
        diccionario_contrasenias[linea[USUARIO]] = linea[CONTRASENIA]
        linea = leer_archivo(contrasenias)
    contrasenias.close()
    
    return diccionario_contrasenias

def cargar_configuracion():
    """Joaquin: Carga la configuración del juego desde un archivo"""
    CLAVE = 0
    VALOR = 1

    with open("configuracion.csv", 'r') as archivo_configuracion:
        lista_de_lineas = archivo_configuracion.readlines()
    
    # Saco el salto de linea al final de cada linea
    # Convierto los valores separados por coma en listas - [clave, valor]
    lista_de_lineas = [linea.rstrip('\n').split(',') for linea in lista_de_lineas]
    
    # {'nombre_del_parametro': valor_del_parametro}
    constantes.configuracion = {linea[CLAVE]:smart_cast(linea[VALOR]) for linea in lista_de_lineas}

    # Si no hay configuracion, uso la configuracion por defecto
    for clave in CONFIGURACION_DEFAULT:
        if clave not in configuracion:
            constantes.configuracion[clave] = CONFIGURACION_DEFAULT[clave]
    
def smart_cast(value):
    """Joaquin: Infiere el tipo de dato a partir de un string y realiza la conversion correspondiente"""
    if value.isnumeric():
        return int(value)
    
    if "True" in value or "False" in value:
        return bool(value)
    
    return value