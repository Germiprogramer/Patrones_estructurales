from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod
import sys
# insertamos la ruta donde se encuentra el directorio de builder
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\builder")
from Pizza import Pizza

class ConstructorPizzaInfantil(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaInfantil()

    @property
    def product(self) -> PizzaInfantil:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> PizzaInfantil:
        return self._product

    def nombre(self) -> None:
        self._product.add("Nombre", "Pizza Infantil")

    def masa(self) -> None:
        self._product.add("Masa", "Masa suave")

    def salsa_base(self) -> None:
        self._product.add("Salsa", "Salsa de tomate suave")

    def ingredientes(self) -> None:
        self._product.add("Ingredientes", "Queso mozzarella, Jamón, Piña")

    def coccion(self) -> None:
        self._product.add("Método de cocción", "Horno")

    def presentacion(self) -> None:
        self._product.add("Detalles de presentación", "Pizza Infantil con caritas de queso")

    def maridaje(self) -> None:
        self._product.add("Maridaje", "Refresco de frutas")

    def extra(self) -> None:
        self._product.add("Extra", "Juguetes sorpresa")

    def precio(self) -> None:
        self._product.add("Precio", 10)


class PizzaInfantil:

    def __init__(self) -> None:
        self.parts = {}

    def add(self, category: str, element: str) -> None:
        self.parts[category] = element

    def list_parts(self) -> None:
        print("Pizza parts:")
        for category, element in self.parts.items():
            print(f"{category}: {element}")
