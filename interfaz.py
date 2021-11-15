from tkinter import *
from tkinter import ttk

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