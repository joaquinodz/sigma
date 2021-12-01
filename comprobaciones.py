import interfaz 
from constantes import YA_INGRESADO, INCORRECTO, INEXISTENTE, CONTRASENIAS_DISTINTAS, NO_VALIDO_CONTRA, NO_VALIDO_USUARIO



def cadena_validada(cadena_a_validar):
    """
    Fátima: recibe el cadena a validar, sea nombre de usuario o contraseña para verificar que no haya tildes
    """

    tildes = ["á", "é", "í", "ó"] 
    cadena_validada = True

    for caracter in cadena_a_validar:
        if caracter in tildes:
            cadena_validada = False

    return cadena_validada

def es_valido_nombre_usuario(nombre_usuario):
    """
    Fátima: recibe el nombre de usuario como paramétro y hace comprobaciones necesarias
    """
    nombre_valido = False
    guiones = "_"
    nombre_usuario_sin_guion = ''.join(caracter for caracter in nombre_usuario if caracter not in guiones)

    if 4 <= len(nombre_usuario) <= 15:
    
        if cadena_validada(nombre_usuario_sin_guion) and nombre_usuario_sin_guion.isalnum():
            nombre_valido = True

    if not nombre_valido:
        interfaz.mensaje_al_usuario(NO_VALIDO_USUARIO)

    return nombre_valido




def es_valida_contrasenia(contrasenia, contrasenia_repetida):
    """ 
    Fátima: recibe la contraseña como paramétro y hace comprobaciones necesarias
    """
    contrasenia_valida = False

    if 8 <= len(contrasenia) <= 12:
        if contrasenia == contrasenia_repetida:
            if cadena_validada(contrasenia) and not contrasenia.islower() and (contrasenia.find("-") != -1 or contrasenia.find("_") != -1) and any(caracter.isdigit() for caracter in contrasenia): 
                contrasenia_valida = True
            else:
                interfaz.mensaje_al_usuario(NO_VALIDO_CONTRA)

        else:
            interfaz.mensaje_al_usuario(CONTRASENIAS_DISTINTAS)
    
    return contrasenia_valida

def usuario_valido(usuario, contrasenia, diccionario_usuarios_contrasenias):
    """
    Rodrigo: primero comprueba que el usuario ingresado se encuentre 
    en la lista de jugadores si lo esta, devuelve un mensaje de error, luego, comprueba la contrasenia mediante contrasenia_comprobada()
    si es valida, devuelve True
    """
    
    if [usuario,0,0] in interfaz.jugadores:
        interfaz.mensaje_al_usuario(YA_INGRESADO)
        jugador_valido = False
    
    else:
        jugador_valido = contrasenia_comprobada(usuario,contrasenia,diccionario_usuarios_contrasenias)

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