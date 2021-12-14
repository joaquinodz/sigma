from tkinter import *
from tkinter import ttk, messagebox
import os
import comprobaciones
import Memotest
import jugador

from util import mezclar_lista
from constantes import EXITO, LISTA_JUGADORES_VACIA, YA_REGISTRADO, NOMBRE, INTENTOS, ACIERTOS, HORAS, MINUTOS, SEGUNDOS
from tablero import reiniciar_tablero 
from manejo_de_archivos import registrar_jugadores_en_archivo, grabar_datos_de_la_partida

nuevos_jugadores_registrados = []

#Interfaz inicial y sus funciones.
def crear_interfaz(configuracion, diccionario_usuarios_contrasenias):
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

    boton_otro_usuario = Button(raiz, text="Ingresar usuario", command= lambda:obtener_jugadores(raiz, entry_nombre_usuario, entry_contrasenia, configuracion, diccionario_usuarios_contrasenias))
    boton_otro_usuario.config(width=22, font=("Courier", 14), bg="whitesmoke")
    boton_otro_usuario.place(x= 290, y=430)

    raiz.mainloop()

def comenzar_el_juego(raiz):
    """Rodrigo: se fija si la lista de jugadores esta vacia, si lo esta, da un mensaje de error, caso contrario, mezcla el orden de jugadores
    y destruye la interfaz"""
    if not jugador.jugadores:
        mensaje_al_usuario(LISTA_JUGADORES_VACIA)
    else:
        mezclar_lista(jugador.jugadores)
        raiz.destroy()

def obtener_jugadores(raiz, nombre, contrasenia, configuracion, diccionario_usuarios_contrasenias):
    """
    Rodrigo: obtiene los jugadores ingresados en la interfaz grafica, comprueba mediante la funcion "usuario_valido", en caso de que 
    pase las comprobaciones appendea al jugador a la lista de jugadores, con sus intentos y puntos inicializados en 0.
    Luego comprueba si la cantidad maxima de jugadores fue alcanzada.
    """

    if comprobaciones.usuario_valido(nombre.get(), contrasenia.get(), diccionario_usuarios_contrasenias):
        jugador.agregar_jugador(nombre.get())
        mensaje_al_usuario(EXITO)
        ventana_jugadores()

        if len(jugador.jugadores) == configuracion["MAXIMO_JUGADORES"]:
            mensaje_al_usuario("Se alcanzo el limite de jugadores, el juego iniciara automaticamente")
            raiz.destroy()

    limpiar_entradas_de_texto(nombre,contrasenia)

#Mensaje jugadores lo cambio a una ventana nueva tipo splash
def ventana_jugadores():
    """
    Fátima: ventana jugadores conectados (ingresados y aceptados)
    """
    raiz = Tk()
    raiz.title("Jugadores aceptados:")
    raiz.geometry("250x250")
    raiz.config(bg="white")
    raiz.resizable(False,False)
    raiz.attributes('-disabled', True)
    
    # NO funciona en Linux
    if os.name != 'posix':
        raiz.iconbitmap("sigma.ico")

    mi_frame= Frame(raiz, width="250", height="250")
    mi_frame.config(bg="white")
    mi_frame.pack()

    jugadores_ingresados = "CONECTADOS: \n{}".format(jugador.obtener_nombres_de_jugadores())
    
    label_jugadores = Label(mi_frame, text = jugadores_ingresados)
    label_jugadores.config(font=("Courier", 14), bg="white", fg ="green") 
    label_jugadores.pack()

    def cerrar_ventana(raiz):
        raiz.quit()
        raiz.destroy()  

    raiz.after(1300,lambda: cerrar_ventana(raiz))
    raiz.mainloop()


#Interfaz de registro y sus funciones.        
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

    boton_jugar = Button(raiz_registro, text="Registrar", command= lambda:registrar_nuevo_usuario(entry_usuario, entry_contrasenia, entry_contrasenia_repetida, diccionario_usuarios_contrasenias))
    boton_jugar.config(width=20, font=("Courier", 14), bg="whitesmoke")
    boton_jugar.place(x= 60, y=430)

    boton_cerrar = Button(raiz_registro, text="Cerrar", command= lambda: registrar_usuarios_en_archivo(raiz_registro))
    boton_cerrar.config(width=20, font=("Courier", 14), bg="whitesmoke")
    boton_cerrar.place(x= 300, y=430) 

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
            jugador.agregar_jugador(nombre_usuario)
            nuevos_jugadores_registrados.append([nombre_usuario, contrasenia])
            diccionario_usuarios_contrasenias[nombre_usuario] = contrasenia
            mensaje_al_usuario(EXITO)
            
        limpiar_entradas_de_texto(entry_usuario, entry_contrasenia, entry_contrasenia_repetida)  
              
    else:
        mensaje_al_usuario(YA_REGISTRADO)
    
def registrar_usuarios_en_archivo(raiz_registro):
    """
    Fátima: registra nuevos usuarios en archivo y cierra ventana registro
    """
    registrar_jugadores_en_archivo(nuevos_jugadores_registrados)
    
    raiz_registro.destroy()


#Interfaz de pantallas finales.
def pantalla_final(configuracion, cantidad_de_partidas_jugadas, tiempo_de_juego):
    """Felipe: Se crea la pantalla final con el resumen del juego."""
    ultima_fila = 0
    raiz = Tk()
    raiz.title("Resultados de la partida.")
    raiz.geometry("560x500")
    raiz.config(bg="white")
    raiz.resizable(False,False)
    
    # NO funciona en Linux
    if os.name != 'posix':
        raiz.iconbitmap("sigma.ico")

    """framesNum = 50 # Numero de frames que tiene el gif
    archivo = "fuegos-artificiales.gif"

    
    frames = [PhotoImage(file=archivo, format='gif -index %i' %(i)) for i in range(framesNum)]

    def update(ind):
        Actualiza la imagen gif
        frame = frames[ind]
        ind += 1
        if ind == framesNum:
            ind = 0
        label.configure(image=frame)
        raiz.after(100, update, ind)

    label = Label(raiz)
    label.pack()
    raiz.after(0, update, 0)"""

    img= PhotoImage(file='fondo.png')
    fondo = ttk.Label(raiz, image=img, anchor="center", background="white")
    fondo.pack(side=TOP, fill=BOTH, padx=10, pady=5)

    mi_frame= Frame(raiz, width="560", height="500")
    mi_frame.config(bg="white")
    mi_frame.pack()

    for usuario in jugador.calcula_ganador():
        if ultima_fila == 0:
            label_jugador = Label(mi_frame, text=f"El ganador es...\n¡{usuario[NOMBRE]}! con {usuario[ACIERTOS]} puntos y {usuario[INTENTOS]} intentos.")
            label_jugador.config(font=("Courier", 14), bg="gold")
            label_jugador.grid(padx=10, pady=10, row=ultima_fila, column=0)
        else:
            label_jugador = Label(mi_frame, text=f"Seguí mejorando \n¡{usuario[NOMBRE]}! obtuviste {usuario[ACIERTOS]} puntos en {usuario[INTENTOS]} intentos.")
            label_jugador.config(font=("Courier", 14), bg="white")
            label_jugador.grid(padx=10, pady=10, row=ultima_fila, column=0)
        ultima_fila += 1

    label_promedio = Label(mi_frame, text=f"Promedio de intentos: {jugador.obtener_promedio_de_intentos()} intentos.")
    label_promedio.config(font=("Courier", 14), fg="green")
    label_promedio.grid(padx=10, pady=10, row=ultima_fila, column=0)
    ultima_fila += 1

    label_tiempo_de_partida = Label(mi_frame, text=f"Tiempo de juego, horas: {tiempo_de_juego[HORAS]}  minutos: {tiempo_de_juego[MINUTOS]}  segundos: {tiempo_de_juego[SEGUNDOS]}")
    label_tiempo_de_partida.config(font=("Courier", 14), fg="green")
    label_tiempo_de_partida.grid(padx=10, pady=10, row=ultima_fila, column=0)
    ultima_fila += 1

    frame_botones = Frame(raiz, width="560", height="500")
    frame_botones.config(bg="white")
    frame_botones.pack()

    boton_terminar = Button(frame_botones, text="Terminar", command= raiz.destroy)
    boton_terminar.config(width=22, font=("Courier", 14), bg="whitesmoke")
    boton_terminar.grid(padx=10, pady=10, row=0, column=0)

    if cantidad_de_partidas_jugadas < configuracion["MAXIMO_PARTIDAS"]:
        boton_otra_partida = Button(frame_botones, text="Continuar", command= lambda:jugar_otra_partida(raiz, configuracion, cantidad_de_partidas_jugadas))
        boton_otra_partida.config(width=22, font=("Courier", 14), bg="whitesmoke")
        boton_otra_partida.grid(padx=10, pady=10, row=0, column=1)

    raiz.mainloop()


def jugar_otra_partida(raiz, configuracion, cantidad_de_partidas_jugadas):
    """Rodrigo: esta funcion destruye la raiz y permite seguir jugando"""
    raiz.destroy()
    grabar_datos_de_la_partida()
    reiniciar_tablero()
    jugador.reiniciar_puntos_e_intentos()
    Memotest.jugar_memotest(configuracion, cantidad_de_partidas_jugadas + 1)

#Funciones generales de interfaz.
def mensaje_al_usuario(mensaje):
    """
    Fátima: cuadro de mensaje ante un error. El mensaje es pasado por parámetro.
    """
    messagebox.showinfo('Atencion!', mensaje) 

def limpiar_entradas_de_texto(*entrys_a_limpiar):
    """
    Fátima: limpia los entrys para un nuevo ingreso
    """
    for entry in entrys_a_limpiar:
        entry.delete(0, 'end')