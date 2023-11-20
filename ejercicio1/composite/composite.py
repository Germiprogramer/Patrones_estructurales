from __future__ import annotations
import sys
# insertamos la ruta donde se encuentra el directorio de builder
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\builder")
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\uml")

# importamos las clases de builder
from Director import Director, to_dict
from pizzas.Pizza_Barbacoa import ConstructorPizzaBarbacoa, PizzaBarbacoa
from pizzas.Pizza_Infantil import ConstructorPizzaInfantil, PizzaInfantil
from Pizza import Pizza
from abc import ABC, abstractmethod
from typing import List
import csv


class Component(ABC):
    @abstractmethod
    def decir_precio(self) -> float:
        pass

class Pizza_Component(Component):
    def __init__(self, pizza: str) -> None:
        self.pizza = pizza
        director = Director()
        builder = self.tipo_de_pizza(self.pizza)
        director.builder = builder
        director.build()
        self.pizza = builder.product
        self.nombre = self.pizza.parts["Nombre"]

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
        elif tipo_de_pizza == "Pizza Personalizada":
            return ConstructorPizzaPersonalizada()
        elif tipo_de_pizza == "Pizza Infantil":
            return ConstructorPizzaInfantil()
        else:
            print("Tipo de pizza no reconocido")
            return None
    
    def list_parts(self) -> None:
        self.pizza.list_parts()

class Entrante_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def decir_precio(self) -> float:
        return self.precio

class Bebida_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def decir_precio(self) -> float:
        return self.precio

class Postre_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
   
    def decir_precio(self) -> float:
        return self.precio

class CompositeMenu(Component):
    def __init__(self, code: int, nombre: str, discount: float = 0.0) -> None:
        self.code = code
        self.nombre = nombre
        self.discount = discount
        self.components = []

    def add_component(self, component: Component) -> None:
        self.components.append(component)

    def remove_component(self, component: Component) -> None:
        self.components.remove(component)

    def decir_precio(self) -> float:
        total_price = sum(component.decir_precio() for component in self.components)
        discounted_price = total_price * (1.0 - self.discount)
        discounted_price = round(discounted_price, 2)
        return discounted_price

    def to_csv(self):
        with open("ejercicio1/datos/pedidos.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            components = []
            for component in self.components:
                components.append(component.nombre)
            writer.writerow([self.code, self.nombre, self.discount, components[0], components[1], components[2], components[3]])

class CompositeMenuCompuesto(Component):
    def __init__(self, code: int, nombre: str, discount: float = 0.0) -> None:
        self.code = code
        self.nombre = nombre
        self.discount = discount
        self.components = []

    def add_component(self, component: Component) -> None:
        self.components.append(component)

    def remove_component(self, component: Component) -> None:
        self.components.remove(component)

    def decir_precio(self) -> float:
        total_price = sum(component.decir_precio() for component in self.components)
        discounted_price = total_price * (1.0 - self.discount)
        discounted_price = round(discounted_price, 2)
        return discounted_price

    def to_csv(self):
        with open("ejercicio1/datos/pedidos.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            components = []
            for menu in self.components:
                components.append(menu.components.nombre)
            writer.writerow([self.code, self.nombre, self.discount, components[0], components[1], components[2], components[3]])
        



menu_infantil = CompositeMenu(1, "MENU_INFANTIL", discount=0.1)
menu_infantil.add_component(Pizza_Component("Pizza Infantil"))
menu_infantil.add_component(Entrante_Component("Patatas fritas", 3.0))
menu_infantil.add_component(Bebida_Component("Refresco", 2.0))
menu_infantil.add_component(Postre_Component("Helado", 2.0))

menu_compuesto = CompositeMenuCompuesto(2,"MENU_COMPUESTO", discount=0.1)
menu_compuesto.add_component(menu_infantil)
menu_compuesto.add_component(menu_infantil)


print(menu_infantil.decir_precio())
print(menu_compuesto.decir_precio())

menu_infantil.to_csv()
menu_compuesto.to_csv()




