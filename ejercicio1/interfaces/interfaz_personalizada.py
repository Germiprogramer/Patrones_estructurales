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
from componentes import Component, Entrante_Component, Bebida_Component, Postre_Component, Pizza_Component, Pizza_Personalizada_Component


import tkinter as tk
from tkinter import messagebox

class Interfaz_Menu_Pers:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizzería Menú")
        self.menu = None

        label = tk.Label(self.master, text="¡Bienvenido a la Pizzería!")
        label.grid(pady=10)

        tk.Label(self.master, text="Realizar Pedido").grid()

        # Pizza attributes options
        options = ["Delgada", "Normal", "Gruesa"]
        self.masa_var = tk.StringVar(self.master)
        self.masa_var.set(options[0])
        tk.Label(self.master, text="Masa").grid()
        masa_menu = tk.OptionMenu(self.master, self.masa_var, *options)
        masa_menu.grid()

        options = ["Tomate", "Blanca"]
        self.salsa_var = tk.StringVar(self.master)
        self.salsa_var.set(options[0])
        tk.Label(self.master, text="Salsa Base").grid()
        salsa_menu = tk.OptionMenu(self.master, self.salsa_var, *options)
        salsa_menu.grid()

        self.ingredientes_var = tk.StringVar(self.master)
        ingredientes_entry = tk.Entry(self.master, textvariable=self.ingredientes_var)
        tk.Label(self.master, text="Ingredientes").grid()
        ingredientes_entry.grid()

        options = ["Suave", "Crujiente", "Crocante"]
        self.coccion_var = tk.StringVar(self.master)
        self.coccion_var.set(options[0])
        tk.Label(self.master, text="Cocción").grid()
        coccion_menu = tk.OptionMenu(self.master, self.coccion_var, *options)
        coccion_menu.grid()

        options = ["Normal", "Premium"]
        self.presentacion_var = tk.StringVar(self.master)
        self.presentacion_var.set(options[0])
        tk.Label(self.master, text="Presentación").grid()
        presentacion_menu = tk.OptionMenu(self.master, self.presentacion_var, *options)
        presentacion_menu.grid()

        options = ["Vino tinto", "Cerveza", "Refresco"]
        self.maridaje_var = tk.StringVar(self.master)
        self.maridaje_var.set(options[0])
        tk.Label(self.master, text="Maridaje").grid()
        maridaje_menu = tk.OptionMenu(self.master, self.maridaje_var, *options)
        maridaje_menu.grid()

        self.extras_var = tk.StringVar(self.master)
        extras_entry = tk.Entry(self.master, textvariable=self.extras_var)
        tk.Label(self.master, text="Extras").grid()
        extras_entry.grid()

        options = ["Patatas fritas", "Ensalada", "Pan de ajo", "Pan de queso", "Pan de ajo y queso"]
        self.entrante = tk.StringVar(self.master)
        self.entrante.set(options[0])
        tk.Label(self.master, text="Entrante").grid()
        entrante_menu = tk.OptionMenu(self.master, self.entrante, *options)
        entrante_menu.grid()

        options = ["Agua", "Refresco", "Cerveza", "Vino tinto", "Vino blanco"]
        self.bebida = tk.StringVar(self.master)
        self.bebida.set(options[0])
        tk.Label(self.master, text="Bebida").grid()
        bebida_menu = tk.OptionMenu(self.master, self.bebida, *options)
        bebida_menu.grid()

        options = ["Helado", "Tarta de queso", "Tarta de chocolate", "Tarta de manzana", "Tarta de zanahoria"]
        self.postre = tk.StringVar(self.master)
        self.postre.set(options[0])
        tk.Label(self.master, text="Postre").grid()
        postre_menu = tk.OptionMenu(self.master, self.postre, *options)
        postre_menu.grid()





        order_button = tk.Button(self.master, text="Realizar Pedido", command=self.place_order)
        order_button.grid()


    def menu_comp(self):
        self.menu = CompositeMenu(1, "MENU_INFANTIL", discount=0.1)
        self.menu.add_component(Pizza_Component("Pizza Infantil"))
        self.menu.add_component(Entrante_Component("Patatas fritas", 3.0))
        self.menu.add_component(Bebida_Component("Refresco", 2.0))
        self.menu.add_component(Postre_Component("Helado", 2.0))
    
    def place_order(self):
        masa = self.masa_var.get()
        salsa_base = self.salsa_var.get()
        ingredientes = self.ingredientes_var.get()
        coccion = self.coccion_var.get()
        presentacion = self.presentacion_var.get()
        maridaje = self.maridaje_var.get()
        extras = self.extras_var.get()
        entrante = self.entrante.get()
        bebida = self.bebida.get()
        postre = self.postre.get()

        self.menu_personalizado = CompositeMenu(1, "MENU_PERSONALIZADO", discount=0.1)
        self.menu_personalizado.add_component(Pizza_Personalizada_Component("Pizza Personalizada",  masa, salsa_base, ingredientes, coccion, presentacion, maridaje, extras))
        self.menu_personalizado.add_component(Entrante_Component(entrante, 3.0))
        self.menu_personalizado.add_component(Bebida_Component(bebida, 2.0))
        self.menu_personalizado.add_component(Postre_Component(postre, 2.0))

        precio = self.menu_personalizado.decir_precio()
        messagebox.showinfo("Pedido Realizado", f"Has pedido el Menú Cuatro Quesos. Precio: ${precio}")
        self.menu_personalizado.to_csv()

        