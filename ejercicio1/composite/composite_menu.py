from __future__ import annotations
from componentes import Component, Entrante_Component, Bebida_Component, Postre_Component, Pizza_Component
import csv

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
            components_list = []
            for menu in self.components:
                for elemento in menu.components:
                    components_list.append(elemento.nombre)
            print(len(components_list))
            pizza = ""
            entrante = ""
            bebida = ""
            postre = ""
            for i in range (0, len(components_list), 4):
                pizza += components_list[i] + " + "
                entrante += components_list[i+1] + " + "
                bebida += components_list[i+2] + " + "
                postre += components_list[i+3] + " + "
            #empleamos slicing para eliminar los ultimos 3 caracteres de cada string y añadimos al csv
            writer.writerow([self.code, self.nombre, self.discount, pizza[:-3], entrante[:-3], bebida[:-3], postre[:-3]])
        

