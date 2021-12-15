import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from manejo_de_archivos import leer_linea

def crear_raiz():
    """
    Joaquin: crea el contexto de la ventana.
    """
    # create root window
    root = tk.Tk()
    root.title('Memotest: Historial de Partidas')
    root.geometry('1080x300')
    root.config(bg="white")
    root.resizable(False,False)

    # NO funciona en Linux
    if os.name != 'posix':
        root.iconbitmap("sigma.ico")

    # configuracion del grid
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    return root

def construir_treeview(raiz):
    """
    Joaquin: crea el contexto de TreeView y setea las columnas que vamos a usar.
    """
    # declaramos las columnas que vamos a usar
    columnas = ('fecha_partida', 'hora_finalizacion', 'nombre_jugador', 'aciertos', 'intentos')

    tree = ttk.Treeview(raiz, columns=columnas, show="headings")
    
    # columna "Fecha"
    tree.heading('fecha_partida', text='Fecha')
    tree.column(column='fecha_partida', width=50, anchor=tk.CENTER)
    
    # columna "Hora"
    tree.heading('hora_finalizacion', text='Hora')
    tree.column(column='hora_finalizacion', width=50, anchor=tk.CENTER)

    # columna "Ganador"
    tree.heading('nombre_jugador', text='Ganador')
    tree.column(column='nombre_jugador', width=50, anchor=tk.CENTER)

    # columna "Intentos"
    tree.heading('intentos', text='Intentos')
    tree.column(column='intentos', width=50, anchor=tk.CENTER)

    # columna "Puntos"
    tree.heading('aciertos', text='Puntos')
    tree.column(column='aciertos', width=50, anchor=tk.CENTER)

    tree.grid(row=0, column=0, sticky='nsew')
    
    return tree

def mostrar_ventana():
    """
    Joaquin: interfaz que muestra un historial de las partidas registradas.
    """
    raiz = crear_raiz()
    
    # vista de arbol de datos
    tree = construir_treeview(raiz)

    # barra de desplazamiento
    scrollbar = ttk.Scrollbar(raiz, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # llenamos la tabla con la información de las partidas
    obtener_partidas(tree)

    # muestro la ventana
    raiz.mainloop()

def obtener_partidas(tree):
    """
    Joaquin: obtiene las partidas registradas en la base de datos y las agrega al TreeView
    """
    archivo = open('partidas.csv', 'r')
    partida = leer_linea(archivo)

    while partida:
        # agregamos los datos de la linea a la lista
        tree.insert('', tk.END, values=partida)

        # leo la siguiente linea
        partida = leer_linea(archivo)

    archivo.close()
