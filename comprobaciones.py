import interfaz

from constantes import YA_INGRESADO, INCORRECTO, INEXISTENTE, CONTRASENIAS_DISTINTAS, NO_VALIDO_CONTRA, NO_VALIDO_USUARIO, NO_ENCONTRADO
from jugador import existe_jugador

def usuario_valido(usuario, contrasenia, diccionario_usuarios_contrasenias):
    """
    Rodrigo: primero comprueba que el usuario ingresado se encuentre 
    en la lista de jugadores si lo esta, devuelve un mensaje de error, luego, comprueba la contrasenia mediante contrasenia_comprobada()
    si es valida, devuelve True
    """
    
    if existe_jugador(usuario):
        interfaz.mensaje_al_usuario(YA_INGRESADO)
        jugador_valido = False
    
    else:
        jugador_valido = contrasenia_comprobada(usuario, contrasenia, diccionario_usuarios_contrasenias)

    return(jugador_valido)

def contrasenia_comprobada(usuario, contrasenia, diccionario_usuarios_contrasenias):
    """Rodrigo: comprueba que el usuario se encuentre en el diccionario de contraseñas, si lo esta, comprueba si la contraseña coincide
    si ambas situaciones se dan, se devuelve True, caso contrario devuelve False y un mensaje apto para cada caso"""
    if usuario in diccionario_usuarios_contrasenias:
            
            if contrasenia == diccionario_usuarios_contrasenias[usuario]:
                contrasenia_validada = True   
            else:
                interfaz.mensaje_al_usuario(INCORRECTO)
                contrasenia_validada = False
        
    else:
        interfaz.mensaje_al_usuario(INEXISTENTE)
        contrasenia_validada = False
    
    return contrasenia_validada


def es_valida_contrasenia(contrasenia, contrasenia_repetida):
    """ 
    Fátima: recibe la contraseña como paramétro y hace comprobaciones necesarias sean de longitud, caracteres válidos o no.
    """
    contrasenia_valida = False

    if 8 <= len(contrasenia) <= 12:
        if contrasenia == contrasenia_repetida:
            if cadena_sin_tildes(contrasenia) and not contrasenia.islower() and (contrasenia.find("-") != NO_ENCONTRADO or contrasenia.find("_") != NO_ENCONTRADO) and any(caracter.isdigit() for caracter in contrasenia): 
                contrasenia_valida = True
            else:
                interfaz.mensaje_al_usuario(NO_VALIDO_CONTRA)

        else:
            interfaz.mensaje_al_usuario(CONTRASENIAS_DISTINTAS)
    
    return contrasenia_valida

def es_valido_nombre_usuario(nombre_usuario):
    """
    Fátima: recibe el nombre de usuario como paramétro y hace comprobaciones necesarias sean de longitud, caracteres válidos o no.
    """
    nombre_valido = False
    caracter_permitido = "_"
    nombre_usuario_sin_guion = ''.join(caracter for caracter in nombre_usuario if caracter not in caracter_permitido)

    if 4 <= len(nombre_usuario) <= 15:
    
        if cadena_sin_tildes(nombre_usuario_sin_guion) and nombre_usuario_sin_guion.isalnum():
            nombre_valido = True

    if not nombre_valido:
        interfaz.mensaje_al_usuario(NO_VALIDO_USUARIO)

    return nombre_valido


def cadena_sin_tildes(cadena_a_validar):
    """
    Fátima: recibe el cadena a validar (nombre de usuario o contraseña) y devuelve True si no contiene tildes
    """

    tildes = ["á", "é", "í", "ó", "ú"] 
    cadena_validada = False
    cadena_a_lista = list(cadena_a_validar.lower())
    caracter = 0

    while cadena_a_lista and caracter < len(cadena_a_lista):

        if not cadena_a_lista[caracter] in tildes:
            cadena_validada = True
        caracter += 1

    return cadena_validada