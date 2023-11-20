from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod
import sys
# insertamos la ruta donde se encuentra el directorio de builder
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\builder")
from Pizza import Pizza

class ConstructorPizzaHawaiana(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaHawaiana()

    @property
    def product(self) -> PizzaHawaiana:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> PizzaHawaiana:
        return self._product

    def nombre(self) -> None:
        self._product.add("Nombre", "Pizza Hawaiana")

    def masa(self) -> None:
        self._product.add("Masa", "Masa")

    def salsa_base(self) -> None:
        self._product.add("Salsa", "Salsa de tomate")

    def ingredientes(self) -> None:
        self._product.add("Ingredientes", "Queso mozzarella, Jamón, Piña")

    def coccion(self) -> None:
        self._product.add("Método de cocción", "Horno")

    def presentacion(self) -> None:
        self._product.add("Detalles de presentación", "Pizza Hawaiana")

    def maridaje(self) -> None:
        self._product.add("Maridaje", "Vino blanco")

    def extra(self) -> None:
        self._product.add("Extra", "Aceite de oliva")

    def precio(self) -> None:
        self._product.add("Precio", 15)


class PizzaHawaiana():

    def __init__(self) -> None:
        self.parts = {}

    def add(self, category: str, element: str) -> None:
        self.parts[category] = element

    def list_parts(self) -> None:
        print("Pizza parts:")
        for category, element in self.parts.items():
            print(f"{category}: {element}")

    