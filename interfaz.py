import random
import os

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

INEXISTENTE = "Usuario inexistente. Por favor, registrese"
INCORRECTO = "Usuario y/o contraseña incorrectos. Ingrese nuevamente."
NO_VALIDO_CONTRA = "Contraseña no válida. Debe contener al menos una letra mayúscula, una letra minúscula, un número, y alguno de los siguientes caracteres: “_” “-“ "
NO_VALIDO_USUARIO = "Usuario no válido. Debe contener como mínimo un largo de 4 caracteres y un máximo de 15, y estar formado sólo por letras, números y el guión bajo."
YA_INGRESADO = "Ese usuario ya ha sido ingresado"
EXITO = "Usuario ingresado con exito"

jugadores = []
jugador_actual = 0

def crear_interfaz():
    """
    Fátima: se crea interfaz gráfica para el ingreso de jugadores.
    """
    raiz = Tk()
    raiz.title("Memotest: pon a prueba tu memoria")
    raiz.geometry("700x530")
    raiz.config(bg="white")
    raiz.resizable(False,False)
    
    # NO funciona en Linux
    if os.name != 'posix':
        raiz.iconbitmap("sigma.ico")

    menubar = Menu(raiz)
    raiz.config(menu=menubar)
    menubar.add_command(label="Registrame", command= lambda:ventana_de_registro())


    img= PhotoImage(file='fondo.png')
    fondo = ttk.Label(raiz, image=img, anchor="center", background="white")
    fondo.pack(side=TOP, fill=BOTH, padx=10, pady=5)

    mi_frame= Frame(raiz, width="700", height="530")
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
    boton_jugar.config(width=20, font=("Courier", 14), bg="whitesmoke")
    boton_jugar.place(x= 10, y=450)

    boton_otro_usuario = Button(raiz, text="Ingresar usuario", command= lambda:obtener_jugadores(entry_nombre_usuario, entry_contrasenia))
    boton_otro_usuario.config(width=22, font=("Courier", 14), bg="whitesmoke")
    boton_otro_usuario.place(x= 250, y=450)
    
    boton_limpiar = Button(raiz, text="Limpiar texto", command= lambda: limpiar(raiz, entry_nombre_usuario, entry_contrasenia))
    boton_limpiar.config(width=15, font=("Courier", 14), bg="whitesmoke")
    boton_limpiar.place(x= 510, y=450)

    raiz.mainloop()
    
    
def limpiar(raiz, entry_nombre_usuario, entry_contrasenia):
    """
    Fátima: limpia los entrys para un nuevo ingreso
    """
    entry_nombre_usuario.delete(0, 'end')
    entry_contrasenia.delete(0, 'end')
    
    
def ventana_de_registro():

    """
    Fátima: se crea interfaz gráfica para el registro de jugadores.
    """

    raiz_registro = Tk()
    raiz_registro.title("Registro de usuario")
    raiz_registro.geometry("500x300")
    raiz_registro.config(bg="white")
    raiz_registro.resizable(False,False)

    # NO funciona en Linux
    if os.name != 'posix':
        raiz_registro.iconbitmap("sigma.ico")

    mi_frame= Frame(raiz_registro, width="500", height="300")
    mi_frame.config(bg="white")
    mi_frame.pack()

    label_inicial = Label(mi_frame, text="Registro de participantes")
    label_inicial.config(font=("Courier", 18), bg="white")
    label_inicial.grid(padx=10, pady=10, row=0, column=0, columnspan=2)

    label_usuario = Label(mi_frame, text="Nombre de usuario")
    label_usuario.config(font=("Courier", 14), bg="white")
    label_usuario.grid(padx=10, pady=10, row=1, column=0)

    entry_usuario = Entry(mi_frame) 
    entry_usuario.config(bg="black", width=27, insertbackground="blue",fg="white",font=10)
    entry_usuario.grid(padx=10, pady=10, row=1, column=1, ipady=6)

    label_contrasenia = Label(mi_frame, text="Contraseña")
    label_contrasenia.config(font=("Courier", 14), bg="white")
    label_contrasenia.grid(padx=10, pady=10, row=2, column=0)

    entry_contrasenia = Entry(mi_frame)
    entry_contrasenia.config(bg="black", width=27, insertbackground="blue", fg="white",font=10)
    entry_contrasenia.grid(padx=10, pady=10, row=2, column=1, ipady=6)

    label_contrasenia_repetida = Label(mi_frame, text="Repetir contraseña")
    label_contrasenia_repetida.config(font=("Courier", 14), bg="white")
    label_contrasenia_repetida.grid(padx=10, pady=10, row=3, column=0)

    entry_contrasenia_repetida = Entry(mi_frame)
    entry_contrasenia_repetida.config(bg="black", width=27, insertbackground="blue", fg="white",font=10)
    entry_contrasenia_repetida.grid(padx=10, pady=10, row=3, column=1, ipady=6)

    boton_jugar = Button(raiz_registro, text="Registrar", command= raiz_registro.destroy)
    boton_jugar.config(width=35, font=("Courier", 14), bg="whitesmoke")
    boton_jugar.pack(side=BOTTOM, fill=BOTH,padx=20, pady=27, ipady=15)   

    raiz_registro.mainloop()

def comenzar_el_juego(raiz):
    global jugadores
    random.shuffle(jugadores)
    raiz.destroy()


def obtener_jugadores(nombre,contrasenia):
    """
    Rodrigo: obtiene los jugadores ingresados en la interfaz grafica, comprueba mediante la funcion "comprobar_usuario", en caso de que 
    pase las comprobaciones appendea al jugador a la lista de jugadores, con sus intentos y puntos inicializados en 0.
    """
    usuario_comprobado = comprobar_usuario(nombre.get(),contrasenia.get())
    if usuario_comprobado:
        global jugadores
        jugadores.append([nombre.get(),0,0])
        mensaje_incorrecto(EXITO)
        ventana_jugadores_aceptados() #Mostrar los usuarios aceptados. Solucionar las muultiples ventanas
        

def comprobar_usuario(usuario , contrasenia):
    """
    Rodrigo: comprueba que el usuario ingresado se encuentre en la lista de jugadores si lo esta, devuelve un mensaje de error, 
    en caso de que no lo este comprueba que este en el archivo de usuarios y contraseñas, en caso de 
    estarlo y que tanto usuario como contraseña coincidan, devuelve True, caso contrario, devuelve False ademas de un mensaje de error dependiendo 
    el caso
    """
    if [usuario,0,0] in jugadores:
        mensaje_incorrecto(YA_INGRESADO)
    
    else:

        with open("contrasenia.csv","r") as archivo_contrasenia:
            usuario_encontrado = False
            contrasenia_correcta = True
            usuario_almacenado , contrasenia_almacenada = leer_Archivo(archivo_contrasenia)

            while usuario_almacenado and contrasenia_correcta and not usuario_encontrado:
                if (usuario_almacenado == usuario):
                    usuario_encontrado = True
                    if contrasenia_almacenada != contrasenia:
                        contrasenia_correcta = False
                            
                else:
                    usuario_almacenado, contrasenia_almacenada = leer_Archivo(archivo_contrasenia)
                
            if not usuario_encontrado:
                mensaje_incorrecto(INEXISTENTE)
                devolver = False
                
            elif usuario_encontrado and not contrasenia_correcta:
                mensaje_incorrecto(INCORRECTO)
                devolver = False
                    
            else:
                devolver = True
            
            archivo_contrasenia.seek(0)

            return devolver
    
def mensaje_incorrecto(mensaje):
    """
    Fátima: cuadro de mensaje ante un error. El mensaje es pasado por parámetro.
    """
    messagebox.showinfo('ERROR!', mensaje) 


def obtener_nombres():
    """
    Fátima: obtener todos los nombres de los jugadores
    """
    nombres = ""
    if jugadores!= "":
        for elemento in jugadores: 
            nombres += elemento[0] +"\n"
    return nombres

def leer_Archivo(archivo):
    """
    Rodrigo: lee un archivo linea a linea
    """
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        return linea.split(',')
    else:
        return None, None 


crear_interfaz()
print(jugadores)
