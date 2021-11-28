from constantes import USUARIO,CONTRASENIA


def leer_archivo(archivo):
    """
    Rodrigo: lee un archivo linea a linea
    """
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        linea_procesada = linea.split(',')
    else:
        linea_procesada =  None, None 

    return linea_procesada


def convertir_contrasenia_a_diccionario():
    """Rodrigo: convierte el archivo de contrasenias a un diccionario"""
    contrasenias = open("contrasenia.csv","r")
    diccionario_contrasenias = {}
    linea = leer_archivo(contrasenias)
    while linea[USUARIO]:
        diccionario_contrasenias[linea[USUARIO]] = linea[CONTRASENIA]
        linea = leer_archivo(contrasenias)
    contrasenias.close()
    
    return diccionario_contrasenias