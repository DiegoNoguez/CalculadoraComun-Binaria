import tkinter as tk
from tkinter import ttk,filedialog,messagebox


#Variables globales
global window

#Declaracion de funciones
def Botonesetiquetas():
    global window
    n1=ttk.Entry()
    n1.place(x=5,y=15,width=275,height=50)

    botonNu1=tk.Button(window, text="1")
    botonNu1.place(x=5,y=85)
    botonNu2=tk.Button(window,text="2")
    botonNu2.place(x=45,y=85)
    botonNu3=tk.Button(window, text="3")
    botonNu3.place(x=85,y=85)

def Ventana():
    global window, n1
    window=tk.Tk()
    window.title("Calculadora")
    window.geometry("450x450")
    Botonesetiquetas()
    window.mainloop()

#Ejecucion del codigo
Ventana()