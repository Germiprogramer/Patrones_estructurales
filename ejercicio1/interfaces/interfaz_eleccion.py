import tkinter as tk
import csv
from tkinter import messagebox
import pandas as pd
from interfaz_menu_ind import Interfaz_Menu_Ind
from interfaz_menu_comp import Interfaz_Menu_Comp
from interfaz_personalizada import Interfaz_Menu_Pers

# Función para que el usuario pueda elegir entre una pizza del menú o una personalizada
def interfaz_eleccion():

    options_window = tk.Tk()
    options_window.title("Opciones")
    
    tk.Label(options_window, text="Elige una opción:").pack(pady=10)
    '''
    # Función para obtener la recomendación de pizza del usuario
    def hacer_recomendacion():
        df = pd.read_csv('ejercicio1/datos/pedidos.csv')

        nombre_usuario = entry_usuario.get()

        df_filtrado = df[df["usuario"] == nombre_usuario]

        dato_mas_repetido = df_filtrado["tipo"].mode().iloc[0]
        
        if str(dato_mas_repetido) != "personalizada":

            print(dato_mas_repetido)
            
            recomendacion = str(dato_mas_repetido)

            resultado.config(text=recomendacion)
        else:
            masa_repetida = df_filtrado["masa"].mode().iloc[0]
            salsa_repetida = df_filtrado["salsa"].mode().iloc[0]
            coccion_repetida = df_filtrado["coccion"].mode().iloc[0]
            presentacion_repetida = df_filtrado["presentacion"].mode().iloc[0]
            maridaje_repetido = df_filtrado["maridaje"].mode().iloc[0]

            resultado.config(text=(masa_repetida, salsa_repetida, coccion_repetida, presentacion_repetida, maridaje_repetido))

    '''
    # Función para mostrar la interfaz del menú
    def menu():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Menú Individual")
        options_window.destroy()  # Cerrar la ventana de opciones
        
        root = tk.Tk()
        Interfaz_Menu_Ind(root)
        


    # Función para mostrar la interfaz de la pizza personalizada
    def combo():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Menú Combo")
        options_window.destroy()  # Cerrar la ventana de opciones

        root = tk.Tk()
        Interfaz_Menu_Comp(root)
    
    # Crear y colocar widgets para la recomendación de pizza
    label_usuario = tk.Label(options_window, text="Usuario:")
    label_usuario.pack(pady=10)
    entry_usuario = tk.Entry(options_window, width=30)
    entry_usuario.pack(pady=10)

    def personalizada():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Menú Personalizado")
        options_window.destroy()

        root = tk.Tk()
        Interfaz_Menu_Pers(root)

    '''
    recomendar_button = tk.Button(options_window, text="Obtener Recomendación", command=hacer_recomendacion)
    recomendar_button.pack(pady=10)

    resultado = tk.Label(options_window, text="")
    resultado.pack(pady=10)
    '''

    menu_button = tk.Button(options_window, text="Menú Individual", command=menu)
    menu_button.pack(pady=10)
    
    custom_button = tk.Button(options_window, text="Menú Combo", command=combo)
    custom_button.pack(pady=10)

    personalizada_button = tk.Button(options_window, text="Menú Personalizado", command=personalizada)
    personalizada_button.pack(pady=10)

    # Mostrar la ventana de opciones
    options_window.mainloop()