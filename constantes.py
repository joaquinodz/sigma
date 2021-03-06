#Constantes del tablero.
IMAGEN_FICHA = 0
ESTADO_FICHA = 1
FICHAS_POR_FILA = 4

#Constantes del Jugador.
NOMBRE = 0
INTENTOS = 1
ACIERTOS = 2

#Constantes del tiempo.
HORAS = 0
MINUTOS = 1
SEGUNDOS = 2

#mensajes al usuario
INEXISTENTE = "Usuario inexistente. Por favor, registrese"
INCORRECTO = "Usuario y/o contraseña incorrectos. Ingrese nuevamente."
NO_VALIDO_CONTRA = "Contraseña no válida. Debe contener al menos una letra mayúscula, una letra minúscula, un número, y alguno de los siguientes caracteres: “_” “-“ "
NO_VALIDO_USUARIO = "Usuario no válido. Debe contener como mínimo un largo de 4 caracteres y un máximo de 15, y estar formado sólo por letras, números y el guión bajo."
YA_INGRESADO = "Ese usuario ya ha sido ingresado"
EXITO = "Usuario ingresado con exito"
LISTA_JUGADORES_VACIA = "No se ha ingresado ningun jugador"
YA_REGISTRADO = "Nombre usuario no disponible. Ingrese otro"
CONTRASENIAS_DISTINTAS = "Las contraseñas no coinciden. Intente nuevamente"

#comprobaciones
NO_ENCONTRADO = -1

#validacion de los usuarios
MAXIMO_JUGADORES = 3
USUARIO = 0
CONTRASENIA = 1

#Constantes de lectura de archivos
CLAVE = 0
VALOR = 1


#Constantes de Configuracion.
CONFIGURACION_DEFAULT = {
    "CANTIDAD_FICHAS" : 16,
    "MAXIMO_JUGADORES": 2,
    "MAXIMO_PARTIDAS": 5,
    "REINICIAR_ARCHIVO_PARTIDAS": False,
}

PROVIENE_DE_ARCHIVO_CONFIGURACION = 0
PROVIENE_DE_CONSTANTES_ESTABLECIDAS = 1