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

    def get_last_id_pedido(self):
            try:
                with open("ejercicio1/datos/pedidos.csv", 'r') as file:
                    reader = csv.reader(file)
                    # Leer el último ID_pedido
                    last_row = list(reader)[-1]
                    last_id_pedido = int(last_row[-1])
                    return last_id_pedido
            except FileNotFoundError:
                # Si el archivo no existe, devolver 0
                return 
            except ValueError:
                return 0

    def to_csv(self):
        last_id_pedido = self.get_last_id_pedido()
        with open("ejercicio1/datos/pedidos.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            components = []
            for component in self.components:
                components.append(component.nombre)
            writer.writerow([self.code, self.nombre, self.discount, components[0], components[1], components[2], components[3], last_id_pedido + 1])

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

    def get_last_id_pedido(self):
            try:
                with open("ejercicio1/datos/pedidos.csv", 'r') as file:
                    reader = csv.reader(file)
                    # Leer el último ID_pedido
                    last_row = list(reader)[-1]
                    last_id_pedido = int(last_row[-1])
                    return last_id_pedido
            except FileNotFoundError:
                # Si el archivo no existe, devolver 0
                return 0

    def to_csv(self):
        last_id_pedido = self.get_last_id_pedido()
        with open("ejercicio1/datos/pedidos.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            components_list = []
            for menu in self.components:
                for elemento in menu.components:
                    components_list.append(elemento.nombre)    
            for i in range (0, len(components_list), 4):
            #empleamos slicing para eliminar los ultimos 3 caracteres de cada string y añadimos al csv
                writer.writerow([self.code, self.nombre, self.discount, components_list[i], components_list[i+1], components_list[i+2], components_list[i+3], last_id_pedido + 1])