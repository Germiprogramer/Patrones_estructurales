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


class Component(ABC):
    @abstractmethod
    def decir_precio(self) -> float:
        pass

# clase pizza
class Pizza_Component(Component):
    def __init__(self, pizza: str) -> None:
        self.pizza = pizza
        director = Director()
        builder = self.tipo_de_pizza(self.pizza)
        director.builder = builder
        director.build()
        self.pizza = builder.product
        self.nombre = pizza

    def decir_precio(self) -> float:
        return self.pizza.parts["Precio"]

    def tipo_de_pizza(self, tipo_de_pizza) -> str:
        if tipo_de_pizza == "Pizza Barbacoa":
            return ConstructorPizzaBarbacoa()
        elif tipo_de_pizza == "Pizza Cuatro Quesos":
            return ConstructorPizzaCuatroQuesos()
        elif tipo_de_pizza == "Pizza Hawaiana":
            return ConstructorPizzaHawaiana()
        elif tipo_de_pizza == "Pizza Margherita":
            return ConstructorPizzaMargherita()
        elif tipo_de_pizza == "Pizza Infantil":
            return ConstructorPizzaInfantil()
        else:
            print("Tipo de pizza no reconocido")
            return None
    
    def list_parts(self) -> None:
        self.pizza.list_parts()

# para cumplir con el principio de responsabilidad unica, se crea una clase para pizza personalizada
class Pizza_Personalizada_Component(Component):
    def __init__(self, nombre, masa, salsa_base, ingredientes, coccion, presentacion, maridaje, extras) -> None:
        self.nombre = nombre
        self.masa = masa
        self.salsa_base = salsa_base
        self.ingredientes = ingredientes
        self.coccion = coccion
        self.presentacion = presentacion
        self.maridaje = maridaje
        self.extras = extras
        director = Director()
        builder = ConstructorPizzaPersonalizada(self.nombre, self.masa, self.salsa_base, self.ingredientes, self.coccion, self.presentacion, self.maridaje, self.extras)
        director.builder = builder
        director.build()
        self.pizza = builder.product
        

    def decir_precio(self) -> float:
        return self.pizza.parts["Precio"]

    def tipo_de_pizza(self, tipo_de_pizza, masa, salsa_base, ingredientes, coccion, presentacion, maridaje, extras) -> str:
        if tipo_de_pizza == "Pizza Personalizada":
            return ConstructorPizzaPersonalizada()
        else:
            print("Tipo de pizza no reconocido")
            return None
    
    def list_parts(self) -> None:
        self.pizza.list_parts()

# clase entrante
class Entrante_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def decir_precio(self) -> float:
        return self.precio

# clase bebida
class Bebida_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def decir_precio(self) -> float:
        return self.precio

# clase postre
class Postre_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
   
    def decir_precio(self) -> float:
        return self.precio