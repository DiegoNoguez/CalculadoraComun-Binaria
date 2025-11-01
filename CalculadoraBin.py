import tkinter as tk
from tkinter import ttk,filedialog,messagebox


# Variables globales
global window

# Declaracion de funciones
def botonesEtiquetas():
    global window
    n1=ttk.Entry()
    n1.place(x=4,y=10)

def Ventana():
    global window, n1
    window=tk.Tk()
    window.title("Calculadora")
    window.geometry("450x450")
    botonesEtiquetas()
    window.mainloop()

# Ejecución o llamada de funciones
Ventana()