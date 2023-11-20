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
from componentes import Component, Entrante_Component, Bebida_Component, Postre_Component

def menu():
    