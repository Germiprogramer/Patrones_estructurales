from __future__ import annotations
import sys
# insertamos la ruta donde se encuentra el directorio de builder
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\builder")
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\uml")

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

class PizzeriaMenuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizzería Menú")
        
        self.menu_infantil = CompositeMenu(1, "MENU_INFANTIL", discount=0.1)
        self.menu_infantil.add_component(Pizza_Component("Pizza Infantil"))
        self.menu_infantil.add_component(Entrante_Component("Patatas fritas", 3.0))
        self.menu_infantil.add_component(Bebida_Component("Refresco", 2.0))
        self.menu_infantil.add_component(Postre_Component("Helado", 2.0))

        self.menu_compuesto = CompositeMenuCompuesto(2,"MENU_COMPUESTO", discount=0.1)
        self.menu_compuesto.add_component(self.menu_infantil)
        self.menu_compuesto.add_component(self.menu_infantil)

        self.create_gui()

    def create_gui(self):
        # Etiqueta
        label = tk.Label(self.master, text="¡Bienvenido a la Pizzería!")
        label.pack(pady=10)

        # Botón para pedir el menú infantil
        button_menu_infantil = tk.Button(self.master, text="Pedir Menú Infantil", command=self.pedir_menu_infantil)
        button_menu_infantil.pack(pady=5)

        # Botón para pedir el menú compuesto
        button_menu_compuesto = tk.Button(self.master, text="Pedir Menú Compuesto", command=self.pedir_menu_compuesto)
        button_menu_compuesto.pack(pady=5)

    def pedir_menu_infantil(self):
        precio = self.menu_infantil.decir_precio()
        messagebox.showinfo("Pedido Realizado", f"Has pedido el Menú Infantil. Precio: ${precio}")
        self.menu_infantil.to_csv()


    def pedir_menu_compuesto(self):
        precio = self.menu_compuesto.decir_precio()
        messagebox.showinfo("Pedido Realizado", f"Has pedido el Menú Compuesto. Precio: ${precio}")
        self.menu_compuesto.to_csv()

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzeriaMenuApp(root)
    root.mainloop()

