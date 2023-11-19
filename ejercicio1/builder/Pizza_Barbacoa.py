from __future__ import annotations
from typing import Any
from Pizza import Pizza
from abc import ABC, abstractmethod

class ConstructorPizzaBarbacoa(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaBarbacoa()

    @property
    def product(self) -> PizzaBarbacoa:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> PizzaBarbacoa:
        return self._product

    def nombre(self) -> None:
        self._product.add("Nombre", "Pizza Barbacoa")

    def masa(self) -> None:
        self._product.add("Masa", "Masa con especias")

    def salsa_base(self) -> None:
        self._product.add("Salsa", "Salsa barbacoa")

    def ingredientes(self) -> None:
        self._product.add("Ingredientes", "Queso cheddar, Pollo a la barbacoa, Cebolla roja, Cilantro fresco")

    def coccion(self) -> None:
        self._product.add("Método de cocción", "Horno")

    def presentacion(self) -> None:
        self._product.add("Detalles de presentación", "Pizza Barbacoa")

    def maridaje(self) -> None:
        self._product.add("Maridaje", "Cerveza artesanal")

    def extra(self) -> None:
        self._product.add("Extra", "Chiles picantes")


class PizzaBarbacoa():

    def __init__(self) -> None:
        self.parts = {}

    def add(self, category: str, element: str) -> None:
        self.parts[category] = element

    def list_parts(self) -> None:
        print("Pizza parts:")
        for category, element in self.parts.items():
            print(f"{category}: {element}")
