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

class Interfaz_Menu_Comp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizzería Menú")
        
        #Menú infantil
        self.menu_infantil = CompositeMenu(1, "MENU_INFANTIL", discount=0.1)
        self.menu_infantil.add_component(Pizza_Component("Pizza Infantil"))
        self.menu_infantil.add_component(Entrante_Component("Patatas fritas", 3.0))
        self.menu_infantil.add_component(Bebida_Component("Refresco", 2.0))
        self.menu_infantil.add_component(Postre_Component("Helado", 2.0))
        #Menú hawaiano
        self.menu_hawaiano = CompositeMenu(3, "MENU_HAWAIANO", discount=0.1)
        self.menu_hawaiano.add_component(Pizza_Component("Pizza Hawaiana"))
        self.menu_hawaiano.add_component(Entrante_Component("Ensalada de Frutas", 4.0))
        self.menu_hawaiano.add_component(Bebida_Component("Jugo de Piña", 2.5))
        self.menu_hawaiano.add_component(Postre_Component("Tarta de Coco", 3.0))
        #Menú cuatro quesos
        self.menu_cuatro_quesos = CompositeMenu(4, "MENU_CUATRO_QUESOS", discount=0.1)
        self.menu_cuatro_quesos.add_component(Pizza_Component("Pizza Cuatro Quesos"))
        self.menu_cuatro_quesos.add_component(Entrante_Component("Ensalada de Queso", 4.0))
        self.menu_cuatro_quesos.add_component(Bebida_Component("Vino Tinto", 2.5))
        self.menu_cuatro_quesos.add_component(Postre_Component("Tarta de Queso", 3.0))
        #Menú margherita
        self.menu_margherita = CompositeMenu(5, "MENU_MARGHERITA", discount=0.1)
        self.menu_margherita.add_component(Pizza_Component("Pizza Margherita"))
        self.menu_margherita.add_component(Entrante_Component("Ensalada de Tomate", 4.0))
        self.menu_margherita.add_component(Bebida_Component("Vino Blanco", 2.5))
        self.menu_margherita.add_component(Postre_Component("Tarta de Manzana", 3.0))
        
        self.create_gui()

    def create_gui(self):
        # Etiqueta
        label = tk.Label(self.master, text="¡Bienvenido a la Pizzería!")
        label.pack(pady=10)

        # Botón para pedir el menú infantil
        button_menu_infantil = tk.Button(self.master, text="Pedir Menú Infantil", command=self.pedir_menu_infantil)
        button_menu_infantil.pack(pady=5)

        # Botón para pedir el menú hawaiano
        button_menu_compuesto = tk.Button(self.master, text="Pedir Menú Hawaiano", command=self.pedir_menu_hawaiano)
        button_menu_compuesto.pack(pady=5)

        # Botón para pedir el menú cuatro quesos
        button_menu_compuesto = tk.Button(self.master, text="Pedir Menú Cuatro Quesos", command=self.pedir_menu_cuatro_quesos)
        button_menu_compuesto.pack(pady=5)

        # Botón para pedir el menú margherita
        button_menu_compuesto = tk.Button(self.master, text="Pedir Menú Margherita", command=self.pedir_menu_margherita)
        button_menu_compuesto.pack(pady=5)

    def pedir_menu_infantil(self):
        precio = self.menu_infantil.decir_precio()
        messagebox.showinfo("Pedido Realizado", f"Has pedido el Menú Infantil. Precio: ${precio}")
        self.menu_infantil.to_csv()

    def pedir_menu_hawaiano(self):
        precio = self.menu_hawaiano.decir_precio()
        messagebox.showinfo("Pedido Realizado", f"Has pedido el Menú Hawaiano. Precio: ${precio}")
        self.menu_hawaiano.to_csv()
    
    def pedir_menu_cuatro_quesos(self):
        precio = self.menu_cuatro_quesos.decir_precio()
        messagebox.showinfo("Pedido Realizado", f"Has pedido el Menú Cuatro Quesos. Precio: ${precio}")
        self.menu_cuatro_quesos.to_csv()
    
    def pedir_menu_margherita(self):
        precio = self.menu_margherita.decir_precio()
        messagebox.showinfo("Pedido Realizado", f"Has pedido el Menú Margherita. Precio: ${precio}")
        self.menu_margherita.to_csv()


