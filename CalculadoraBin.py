import tkinter as tk
from tkinter import ttk,filedialog,messagebox


#Variables globales
global window

#Declaracion de funciones
def Botonesetiquetas():
    global window
    n1=ttk.Entry()
    n1.place(x=4,y=10)

def Ventana():
    global window, n1
    window=tk.Tk()
    window.title("Calculadora")
    window.geometry("450x450")
    Botonesetiquetas()
    window.mainloop()

#Ejecucion del codigo
Ventana()