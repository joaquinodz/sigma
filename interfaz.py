import random
import os
import comprobaciones
import constantes 
import Memotest
import tablero

from tkinter import *
from tkinter import ttk, messagebox

from constantes import EXITO, LISTA_JUGADORES_VACIA, YA_REGISTRADO, NOMBRE, INTENTOS, ACIERTOS

jugadores = []
jugador_actual = 0

def crear_interfaz(diccionario_usuarios_contrasenias):

    """
    Fátima: se crea interfaz gráfica para el ingreso de jugadores.
    """
    raiz = Tk()
    raiz.title("Memotest: pon a prueba tu memoria")
    raiz.geometry("560x500")
    raiz.config(bg="white")
    raiz.resizable(False,False)
    
    # NO funciona en Linux
    if os.name != 'posix':
        raiz.iconbitmap("sigma.ico")

    menubar = Menu(raiz)
    raiz.config(menu=menubar)
    menubar.add_command(label="Registrame", command= lambda:ventana_de_registro(diccionario_usuarios_contrasenias))


    img= PhotoImage(file='fondo.png')
    fondo = ttk.Label(raiz, image=img, anchor="center", background="white")
    fondo.pack(side=TOP, fill=BOTH, padx=10, pady=5)

    mi_frame= Frame(raiz, width="560", height="500")
    mi_frame.config(bg="white")
    mi_frame.pack()

    
    label_inicial = Label(mi_frame, text="Ingreso de jugadores")
    label_inicial.config(font=("Courier", 18), bg="white")
    label_inicial.grid(padx=10, pady=10, row=0, column=0, columnspan=2)

    label_nombre_usuario = Label(mi_frame, text="Nombre de usuario")
    label_nombre_usuario.config(font=("Courier", 14), bg="white")
    label_nombre_usuario.grid(padx=10, pady=10, row=1, column=0)

    entry_nombre_usuario = Entry(mi_frame) 
    entry_nombre_usuario.config(bg="black", width=35, insertbackground="blue",fg="white",font=10)
    entry_nombre_usuario.grid(padx=10, pady=10, row=1, column=1, ipady=8)

    label_contrasenia = Label(mi_frame, text="Contraseña")
    label_contrasenia.config(font=("Courier", 14), bg="white")
    label_contrasenia.grid(padx=10, pady=10, row=2, column=0)

    entry_contrasenia = Entry(mi_frame)
    entry_contrasenia.config(bg="black", width=35, insertbackground="blue", fg="white",font=10)
    entry_contrasenia.grid(padx=10, pady=10, row=2, column=1, ipady=8)

    boton_jugar = Button(raiz, text="¡Comenzar el juego!", command= lambda:comenzar_el_juego(raiz))
    boton_jugar.config(width=22, font=("Courier", 14), bg="whitesmoke")
    boton_jugar.place(x= 20, y=430)

    boton_otro_usuario = Button(raiz, text="Ingresar usuario", command= lambda:obtener_jugadores(raiz, entry_nombre_usuario, entry_contrasenia,diccionario_usuarios_contrasenias))
    boton_otro_usuario.config(width=22, font=("Courier", 14), bg="whitesmoke")
    boton_otro_usuario.place(x= 290, y=430)

    raiz.mainloop()
    
def limpiar_entradas_de_texto(*entrys_a_limpiar):
    """
    Fátima: limpia los entrys para un nuevo ingreso
    """
    for entry in entrys_a_limpiar:
        entry.delete(0, 'end')
         
def ventana_de_registro(diccionario_usuarios_contrasenias):

    """
    Fátima: se crea interfaz gráfica para el registro de jugadores.
    """

    raiz_registro = Tk()
    raiz_registro.title("Registro de usuario")
    raiz_registro.geometry("600x500")
    raiz_registro.config(bg="white")
    raiz_registro.resizable(False,False)

    # NO funciona en Linux
    if os.name != 'posix':
        raiz_registro.iconbitmap("sigma.ico")

    mi_frame= Frame(raiz_registro, width="600", height="500")
    mi_frame.config(bg="white")
    mi_frame.pack()

    label_inicial = Label(mi_frame, text="Registro de participantes")
    label_inicial.config(font=("Courier", 18), bg="white")
    label_inicial.grid(padx=10, pady=10, row=0, column=0, columnspan=2)

    label_requisitos_nombre = Label(mi_frame, text="El nombre debe tener una longitud entre 4 y 15 caracteres,\n y estar formado sólo por letras, números y el guión bajo.")
    label_requisitos_nombre.config(font=("Courier", 11), bg="white")
    label_requisitos_nombre.grid(padx=10, pady=10, row=1, column=0, columnspan=2)

    label_requisitos_contrasenia = Label(mi_frame, text="La contraseña debe tener una longitud entre 8 y 12 caracteres, \nal menos una letra mayúscula, una letra minúscula,\n un número, y alguno de los siguientes caracteres: “_” “-“")
    label_requisitos_contrasenia.config(font=("Courier", 11), bg="white")
    label_requisitos_contrasenia.grid(padx=10, pady=10, row=2, column=0, columnspan=2)

    label_usuario = Label(mi_frame, text="Nombre de usuario")
    label_usuario.config(font=("Courier", 14), bg="white")
    label_usuario.grid(padx=10, pady=10, row=3, column=0)

    entry_usuario = Entry(mi_frame) 
    entry_usuario.config(bg="black", width=27, insertbackground="blue",fg="white",font=10)
    entry_usuario.grid(padx=10, pady=10, row=3, column=1, ipady=6)

    label_contrasenia = Label(mi_frame, text="Contraseña")
    label_contrasenia.config(font=("Courier", 14), bg="white")
    label_contrasenia.grid(padx=10, pady=10, row=4, column=0)

    entry_contrasenia = Entry(mi_frame)
    entry_contrasenia.config(bg="black", width=27, insertbackground="blue", fg="white",font=10)
    entry_contrasenia.grid(padx=10, pady=10, row=4, column=1, ipady=6)

    label_contrasenia_repetida = Label(mi_frame, text="Repetir contraseña")
    label_contrasenia_repetida.config(font=("Courier", 14), bg="white")
    label_contrasenia_repetida.grid(padx=10, pady=10, row=5, column=0)

    entry_contrasenia_repetida = Entry(mi_frame)
    entry_contrasenia_repetida.config(bg="black", width=27, insertbackground="blue", fg="white",font=10)
    entry_contrasenia_repetida.grid(padx=10, pady=10, row=5, column=1, ipady=6)

    boton_jugar = Button(raiz_registro, text="Registrar", command= lambda:registrar_nuevo_usuario(entry_usuario,entry_contrasenia, entry_contrasenia_repetida, diccionario_usuarios_contrasenias))
    boton_jugar.config(width=35, font=("Courier", 14), bg="whitesmoke")
    boton_jugar.pack(side=BOTTOM, fill=BOTH,padx=20, pady=27, ipady=15)   

    raiz_registro.mainloop()

def registrar_nuevo_usuario(entry_usuario, entry_contrasenia, entry_contrasenia_repetida, diccionario_usuarios_contrasenias):
    """
    Fátima: se registra nuevo usuario si tanto el nombre de usuario como la contraseña son válidas. A su vez, se suma usuario
    a la lista de jugadores de la partida y al diccionario con los datos de los usuarios
    """
    lista_usuarios = diccionario_usuarios_contrasenias.keys()
    nombre_usuario = entry_usuario.get()
    contrasenia = entry_contrasenia.get()
    contrasenia_repetida = entry_contrasenia_repetida.get()
    
    if nombre_usuario not in lista_usuarios:
        
        if comprobaciones.es_valida_contrasenia(contrasenia, contrasenia_repetida) and comprobaciones.es_valido_nombre_usuario(nombre_usuario):
            jugadores.append([nombre_usuario,0,0])
            diccionario_usuarios_contrasenias[nombre_usuario] = contrasenia
            mensaje_al_usuario(EXITO)
        limpiar_entradas_de_texto(entry_usuario, entry_contrasenia, entry_contrasenia_repetida)  
              
    else:
        mensaje_al_usuario(YA_REGISTRADO)

def comenzar_el_juego(raiz):
    """Rodrigo: se fija si la lista de jugadores esta vacia, si lo esta, da un mensaje de error, caso contrario, mezcla el orden de jugadores
    y destruye la interfaz"""
    global jugadores
    if not jugadores:
        mensaje_al_usuario(LISTA_JUGADORES_VACIA)
    else:
        random.shuffle(jugadores)
        raiz.destroy()

def obtener_jugadores(raiz ,nombre,contrasenia,diccionario_usuarios_contrasenias):
    """
    Rodrigo: obtiene los jugadores ingresados en la interfaz grafica, comprueba mediante la funcion "usuario_valido", en caso de que 
    pase las comprobaciones appendea al jugador a la lista de jugadores, con sus intentos y puntos inicializados en 0.
    Luego comprueba si la cantidad maxima de jugadores fue alcanzada.
    """

    if comprobaciones.usuario_valido(nombre.get(),contrasenia.get(),diccionario_usuarios_contrasenias):
        global jugadores
        jugadores.append([nombre.get(),0,0])
        mensaje_al_usuario(EXITO)
        ventana_jugadores()

        if len(jugadores) == constantes.configuracion["MAXIMO_JUGADORES"]:
            mensaje_al_usuario("Se alcanzo el limite de jugadores, el juego iniciara automaticamente")
            raiz.destroy()

    limpiar_entradas_de_texto(nombre,contrasenia)
                  
def mensaje_al_usuario(mensaje):
    """
    Fátima: cuadro de mensaje ante un error. El mensaje es pasado por parámetro.
    """
    messagebox.showinfo('Atencion!', mensaje) 

def obtener_nombres():
    """
    Fátima: obtener todos los nombres de los jugadores
    """
    nombres = ""
    if jugadores:
        for jugador in jugadores: 
            nombres += jugador[NOMBRE] +"\n"
    return nombres

#Mensaje jugadores lo cambio a una ventana nueva tipo splash
def ventana_jugadores():
    raiz = Tk()
    raiz.title("Jugadores aceptados:")
    raiz.geometry("250x250")
    raiz.config(bg="white")
    raiz.resizable(False,False)
    
    # NO funciona en Linux
    if os.name != 'posix':
        raiz.iconbitmap("sigma.ico")

    mi_frame= Frame(raiz, width="250", height="250")
    mi_frame.config(bg="white")
    mi_frame.pack()

    jugadores_ingresados = "CONECTADOS: \n{}".format(obtener_nombres())
    
    label_jugadores = Label(mi_frame, text = jugadores_ingresados)
    label_jugadores.config(font=("Courier", 14), bg="white", fg ="green") 
    label_jugadores.pack()

    def cerrar_ventana(raiz):
        raiz.quit()
        raiz.destroy()  

    raiz.after(1500,lambda: cerrar_ventana(raiz))
    raiz.mainloop()
    

def pantalla_final(cantidad_de_partidas_jugadas):
    ultima_fila = 0
    raiz = Tk()
    raiz.title("Resultados de la partida.")
    raiz.geometry("560x500")
    raiz.config(bg="white")
    raiz.resizable(False,False)
    
    # NO funciona en Linux
    if os.name != 'posix':
        raiz.iconbitmap("sigma.ico")

    framesNum = 50 # Numero de frames que tiene el gif
    archivo = "fuegos-artificiales.gif"

    # Lista de todas las imagenes del gif
    frames = [PhotoImage(file=archivo, format='gif -index %i' %(i)) for i in range(framesNum)]

    def update(ind):
        """ Actualiza la imagen gif """
        frame = frames[ind]
        ind += 1
        if ind == framesNum:
            ind = 0
        label.configure(image=frame)
        raiz.after(100, update, ind) # Numero que regula la velocidad del gif

    label = Label(raiz)
    label.pack()
    raiz.after(0, update, 0)

    """img= PhotoImage(file='fondo.png')
    fondo = ttk.Label(raiz, image=img, anchor="center", background="white")
    fondo.pack(side=TOP, fill=BOTH, padx=10, pady=5)"""

    mi_frame= Frame(raiz, width="560", height="500")
    mi_frame.config(bg="white")
    mi_frame.pack()

    calcula_ganador()
    for jugador in jugadores:
        if ultima_fila == 0:
            label_jugador = Label(mi_frame, text=f"El ganador es...\n¡{jugadores[0][NOMBRE]}! con {jugadores[0][ACIERTOS]} puntos y {jugadores[0][INTENTOS]} intentos.")
            label_jugador.config(font=("Courier", 14), bg="gold")
            label_jugador.grid(padx=10, pady=10, row=ultima_fila, column=0, columnspan=2)
        else:
            label_jugador = Label(mi_frame, text=f"Seguí mejorando \n¡{jugador[NOMBRE]}! obtuviste {jugador[ACIERTOS]} puntos en {jugador[INTENTOS]} intentos.")
            label_jugador.config(font=("Courier", 14), bg="white")
            label_jugador.grid(padx=10, pady=10, row=ultima_fila, column=0)
        ultima_fila += 1

    label_promedio = Label(mi_frame, text=f"Promedio de intentos: {promedio_de_intentos()} intentos.")
    label_promedio.config(font=("Courier", 14), fg="green")
    label_promedio.grid(padx=10, pady=10, row=ultima_fila, column=0)

    boton_jugar = Button(raiz, text="Terminar", command= lambda:raiz.destroy())
    boton_jugar.config(width=22, font=("Courier", 14), bg="whitesmoke")
    boton_jugar.place(x= 20, y=440)


    if cantidad_de_partidas_jugadas < constantes.configuracion["MAXIMO_PARTIDAS"]:
        boton_otro_usuario = Button(raiz, text="Continuar", command= lambda:jugar_otra_partida(raiz,cantidad_de_partidas_jugadas))
        boton_otro_usuario.config(width=22, font=("Courier", 14), bg="whitesmoke")
        boton_otro_usuario.place(x= 290, y=440)

    raiz.mainloop()

def calcula_ganador():
    """Felipe: Ordena la lista de jugadores segun sus aciertos y en caso de empatar segun sus intentos."""
    jugadores.sort(reverse=True, key=lambda jugador: (jugador[ACIERTOS], -jugador[INTENTOS]))

def promedio_de_intentos():
    """Felipe: Se calcula el promedio de intentos de los jugadores en la partida."""
    total_intentos = 0
    for jugador in jugadores:
        total_intentos += jugador[INTENTOS]

    return total_intentos / len(jugadores)


def jugar_otra_partida(raiz,cantidad_de_partidas_jugadas):
    """Rodrigo: esta funcion destruye la raiz y permite seguir jugando"""
    raiz.destroy()
    tablero.reiniciar_tablero()
    Memotest.jugar_memotest(cantidad_de_partidas_jugadas+1)
    