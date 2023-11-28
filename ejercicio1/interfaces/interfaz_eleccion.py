import sys
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\datos\pedidos.csv")
import tkinter as tk
import csv
from tkinter import messagebox
import pandas as pd
from interfaces.interfaz_menu_ind import Interfaz_Menu_Ind
from interfaces.interfaz_menu_comp import Interfaz_Menu_Comp
from interfaces.interfaz_personalizada import Interfaz_Menu_Pers

# Función para que el usuario pueda elegir entre una pizza del menú o una personalizada
def interfaz_eleccion():

    options_window = tk.Tk()
    options_window.title("Opciones")
    
    tk.Label(options_window, text="Elige una opción:").pack(pady=10)

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

    def personalizada():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Menú Personalizado")
        options_window.destroy()

        root = tk.Tk()
        Interfaz_Menu_Pers(root)

    def buscar_pedido():
        pedido = entry_pedido.get()
        pedidos_encontrados = []
        # Abrir el archivo CSV y buscar el pedido
        with open('ejercicio1/datos/pedidos.csv', newline='', encoding='latin-1') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                if row['id_pedido'] == pedido:
                    pedidos_encontrados.append(row)
        if pedidos_encontrados:
            for pedido in pedidos_encontrados:
                mostrar_resultados(pedido)
        else:
            # Mostrar mensaje si el pedido no se encuentra
            text_resultados.delete(1.0, tk.END)  # Limpiar el widget Text
            text_resultados.insert(tk.END, f'Pedido con ID {pedido} no encontrado')

    def mostrar_resultados(pedido):
    # Mostrar las partes más importantes del pedido en el widget Text  # Limpiar el widget Text
        detalles_pedido = f'''{pedido['nombre']}, {pedido['pizza']}, {pedido['entrante']}, {pedido['bebida']}, {pedido['postre']}'''
        text_resultados.insert(tk.END, detalles_pedido)
            

    # Crear y colocar widgets para la recuperación de pedido
    label_pedido = tk.Label(options_window, text="Si quieres reconstruir el pedido, selecciona el número de pedido:")
    label_pedido.pack(pady=10)
    entry_pedido = tk.Entry(options_window, width=30)
    entry_pedido.pack(pady=10)
    pedido_button = tk.Button(options_window, text="Reconstruir pedido", command=buscar_pedido)
    pedido_button.pack(pady=10)

    menu_button = tk.Button(options_window, text="Menú Individual", command=menu)
    menu_button.pack(pady=10)

    text_resultados = tk.Text(options_window, height=7, width=50)
    text_resultados.pack(pady=10)
    
    custom_button = tk.Button(options_window, text="Menú Combo", command=combo)
    custom_button.pack(pady=10)

    personalizada_button = tk.Button(options_window, text="Menú Personalizado", command=personalizada)
    personalizada_button.pack(pady=10)

    # Mostrar la ventana de opciones
    options_window.mainloop()