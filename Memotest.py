import time
import random
from tkinter import *
from tkinter import ttk

from util import limpiar_consola, tiempo_de_juego
from tablero import inicializar_tablero, refresca_tablero, pedir_datos, finalizar, IMAGEN_FICHA, ESTADO_FICHA, CANTIDAD_DE_FICHAS
from jugador import procesar_resultados, NOMBRE

def obtener_jugadores(raiz,jugador_uno,jugador_dos):
    INTENTOS = 0
    PUNTOS = 0
    """
    Rodrigo: obtiene los jugadores ingresados en la interfaz grafica, genera la lista de jugadores
    con sus puntos y sus intentos, la mezcla para ser almacenada en una variable global
    """
    global lista_jugadores
    lista_jugadores = [[jugador_uno.get(),INTENTOS,PUNTOS],[jugador_dos.get(),INTENTOS,PUNTOS]]
    random.shuffle(lista_jugadores)
    raiz.destroy()
    
def crear_interfaz():
    """
    Fátima: se crea interfaz gráfica para el ingreso de jugadores.
    """
    raiz = Tk()
    raiz.title("Memotest: pon a prueba tu memoria")
    raiz.iconbitmap("sigma.ico")
    raiz.geometry("500x500")
    raiz.config(bg="white")
    raiz.resizable(False,False)
    
    img= PhotoImage(file='fondo.png')
    fondo = ttk.Label(raiz, image=img, anchor="center", background="white")
    fondo.pack(side=TOP, fill=BOTH, padx=10, pady=5)

    mi_frame= Frame(raiz, width="500", height="500")
    mi_frame.config(bg="white")
    mi_frame.pack()

    label_inicial = Label(mi_frame, text="Ingreso de participantes")
    label_inicial.config(font=("Courier", 18), bg="white")
    label_inicial.grid(padx=10, pady=10, row=0, column=0, columnspan=2)

    label_jugador_uno = Label(mi_frame, text="Jugador")
    label_jugador_uno.config(font=("Courier", 14), bg="white")
    label_jugador_uno.grid(padx=10, pady=10, row=1, column=0)

    entry_jugador_uno = Entry(mi_frame) 
    entry_jugador_uno.config(bg="black", width=35, insertbackground="blue",fg="white",font=10)
    entry_jugador_uno.grid(padx=10, pady=10, row=1, column=1, ipady=8)

    label_jugador_dos = Label(mi_frame, text="Jugador")
    label_jugador_dos.config(font=("Courier", 14), bg="white")
    label_jugador_dos.grid(padx=10, pady=10, row=2, column=0)

    entry_jugador_dos = Entry(mi_frame)
    entry_jugador_dos.config(bg="black", width=35, insertbackground="blue", fg="white",font=10)
    entry_jugador_dos.grid(padx=10, pady=10, row=2, column=1, ipady=8)

    boton_jugar = Button(raiz, text="¡Comenzar el juego!", command= lambda:obtener_jugadores(raiz, entry_jugador_uno, entry_jugador_dos))
    boton_jugar.config(width=35, font=("Courier", 14), bg="whitesmoke")
    boton_jugar.pack(side=BOTTOM, fill=BOTH,padx=20, pady=20, ipady=15)   

    raiz.mainloop()

def memotest_juego(tablero, jugadores):
    jugador_actual_id = 0

    while not finalizar(tablero):
        print(f"Turno de {jugadores[jugador_actual_id][NOMBRE]}")
        refresca_tablero(tablero)

        # Solicitamos al usuario la 1° posicion, validamos el valor y mostramos la ficha seleccionada
        primera_posicion = pedir_datos("1° Posición: ", tablero)

        # Solicitamos al usuario la 2° posicion, validamos el valor y mostramos la ficha seleccionada
        segunda_posicion = pedir_datos("2° Posición: ", tablero)
        
        procesar_resultados(tablero, jugadores, jugador_actual_id, (primera_posicion, segunda_posicion))
        finalizar_turno(tablero)

        # Ahora es turno del otro jugador (TODO: mejorarlo un toque)
        jugador_actual_id = (1 - jugador_actual_id)

def finalizar_turno(tablero):
    """
    Joaquin: Ejecuta las tareas necesarias para finalizar el turno
    """
    time.sleep(2)
    limpiar_consola()

def main():
    """
    tablero es una lista cuyos elementos representan cada "casillero" de el tablero
    cada casillero tiene a su vez una lista con dos valores
    el primer valor representa la imagen que tiene el casillero
    y el segundo valor representa si esta descubierto o no.
    """
    jugadores = [["juan", 0, 0], ["manuel", 0, 0]]
    tablero = inicializar_tablero(CANTIDAD_DE_FICHAS)
    inicio = time.time()

    memotest_juego(tablero, jugadores)

    tiempo_de_juego(inicio)
    
    crear_interfaz()

main()
