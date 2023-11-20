from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod
import sys
# insertamos la ruta donde se encuentra el directorio de builder
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\builder")
from Pizza import Pizza

class ConstructorPizzaMargherita(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaMargherita()

    @property
    def product(self) -> PizzaMargherita:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> PizzaMargherita:
        return self._product

    def nombre(self) -> None:
        self._product.add("Nombre", "Pizza Margherita")

    def masa(self) -> None:
        self._product.add("Masa", "Masa fina")

    def salsa_base(self) -> None:
        self._product.add("Salsa", "Salsa de tomate")

    def ingredientes(self) -> None:
        self._product.add("Ingredientes", "Queso mozzarella, Albahaca fresca")

    def coccion(self) -> None:
        self._product.add("Método de cocción", "Horno")

    def presentacion(self) -> None:
        self._product.add("Detalles de presentación", "Pizza Margherita")

    def maridaje(self) -> None:
        self._product.add("Maridaje", "Vino tinto")

    def extra(self) -> None:
        self._product.add("Extra", "Aceite de oliva")

    def precio(self) -> None:
        self._product.add("Precio", 15)


class PizzaMargherita():

    def __init__(self) -> None:
        self.parts = {}

    def add(self, category: str, element: str) -> None:
        self.parts[category] = element

    def list_parts(self) -> None:
        print("Pizza parts:")
        for category, element in self.parts.items():
            print(f"{category}: {element}")

    
