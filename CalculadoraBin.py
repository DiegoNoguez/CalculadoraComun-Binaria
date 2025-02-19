import tkinter as tk

#Variables globales
global ventana

#Declaracion de funciones
def Ventana():
    ventana=tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("450x450")
    ventana.mainloop()

#Ejecucion del codigo
Ventana()