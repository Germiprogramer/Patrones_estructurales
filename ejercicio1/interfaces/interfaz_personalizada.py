from __future__ import annotations
import sys
# insertamos la ruta donde se encuentra el directorio de builder
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\builder")
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\uml")
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\composite")


# importamos las clases de builder
from Director import Director, to_dict
from pizzas.Pizza_Barbacoa import ConstructorPizzaBarbacoa, PizzaBarbacoa
from pizzas.Pizza_Infantil import ConstructorPizzaInfantil, PizzaInfantil
from pizzas.Pizza_CuatroQuesos import ConstructorPizzaCuatroQuesos, PizzaCuatroQuesos
from pizzas.Pizza_Hawaiana import ConstructorPizzaHawaiana, PizzaHawaiana
from pizzas.Pizza_Margherita import ConstructorPizzaMargherita, PizzaMargherita
from pizzas.Pizza_Personalizada import ConstructorPizzaPersonalizada, PizzaPersonalizada
from Pizza import Pizza
from abc import ABC, abstractmethod
import csv
from composite_menu import CompositeMenu, CompositeMenuCompuesto
from componentes import Component, Entrante_Component, Bebida_Component, Postre_Component, Pizza_Component


import tkinter as tk
from tkinter import messagebox

class Interfaz_Menu_Pers:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizzería Menú")
        self.menu = None
        self.create_gui()

    def menu_comp(self):
        self.menu = CompositeMenu(1, "MENU_INFANTIL", discount=0.1)
        self.menu.add_component(Pizza_Component("Pizza Infantil"))
        self.menu.add_component(Entrante_Component("Patatas fritas", 3.0))
        self.menu.add_component(Bebida_Component("Refresco", 2.0))
        self.menu.add_component(Postre_Component("Helado", 2.0))
    
    def create_gui(self):
        label = tk.Label(self.master, text="¡Bienvenido a la Pizzería!")
        label.grid(pady=10)

        tk.Label(self.master, text="Realizar Pedido").grid()

        # Pizza attributes options
        options = ["Delgada", "Normal", "Gruesa"]
        masa_var = tk.StringVar(self.master)
        masa_var.set(options[0])
        tk.Label(self.master, text="Masa").grid()
        masa_menu = tk.OptionMenu(self.master, masa_var, *options)
        masa_menu.grid()

        options = ["Tomate", "Blanca"]
        salsa_var = tk.StringVar(self.master)
        salsa_var.set(options[0])
        tk.Label(self.master, text="Salsa Base").grid()
        salsa_menu = tk.OptionMenu(self.master, salsa_var, *options)
        salsa_menu.grid()

        ingredientes_var = tk.StringVar(self.master)
        ingredientes_entry = tk.Entry(self.master, textvariable=ingredientes_var)
        tk.Label(self.master, text="Ingredientes").grid()
        ingredientes_entry.grid()

        options = ["Suave", "Crujiente", "Crocante"]
        coccion_var = tk.StringVar(self.master)
        coccion_var.set(options[0])
        tk.Label(self.master, text="Cocción").grid()
        coccion_menu = tk.OptionMenu(self.master, coccion_var, *options)
        coccion_menu.grid()

        options = ["Normal", "Premium"]
        presentacion_var = tk.StringVar(self.master)
        presentacion_var.set(options[0])
        tk.Label(self.master, text="Presentación").grid()
        presentacion_menu = tk.OptionMenu(self.master, presentacion_var, *options)
        presentacion_menu.grid()

        options = ["Vino tinto", "Cerveza", "Refresco"]
        maridaje_var = tk.StringVar(self.master)
        maridaje_var.set(options[0])
        tk.Label(self.master, text="Maridaje").grid()
        maridaje_menu = tk.OptionMenu(self.master, maridaje_var, *options)
        maridaje_menu.grid()

        extras_var = tk.StringVar(self.master)
        extras_entry = tk.Entry(self.master, textvariable=extras_var)
        tk.Label(self.master, text="Extras").grid()
        extras_entry.grid()

        order_button = tk.Button(self.master, text="Realizar Pedido", command=place_order)
        order_button.grid()
    