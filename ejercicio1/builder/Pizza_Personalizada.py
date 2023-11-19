from __future__ import annotations
from typing import Any
from Pizza import Pizza
from abc import ABC, abstractmethod

class ConstructorPizzaPersonalizada(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaPersonalizada()

    @property
    def product(self) -> PizzaPersonalizada:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> PizzaPersonalizada:
        return self._product

    def nombre(self) -> None:
        nombre = input("Ingrese el nombre de la pizza: ")
        self._product.add("Nombre", str(nombre))
        

    def masa(self) -> None:
        masa = str(input("Elige el tipo de masa (fina, normal, gruesa): "))
        if masa == "fina" or masa == "normal" or masa == "gruesa":
            self._product.add("Masa", masa)
        else:
            print("Tipo de masa no válido")
            self.masa()
        

    def salsa_base(self) -> None:
        salsa = str(input("Elige el tipo de salsa (tomate, barbacoa, pesto): "))
        if salsa == "tomate" or salsa == "barbacoa" or salsa == "pesto":
            self._product.add("Salsa", salsa)
        else:
            print("Tipo de salsa no válido")
            self.salsa_base()

    def ingredientes(self) -> None:
        ingredientes = str(input("Elige los ingredientes (queso, jamón, piña, pollo, cebolla, cilantro, chiles, aceitunas, albahaca): "))
        if ingredientes == "queso" or ingredientes == "jamón" or ingredientes == "piña" or ingredientes == "pollo" or ingredientes == "cebolla" or ingredientes == "cilantro" or ingredientes == "chiles" or ingredientes == "aceitunas" or ingredientes == "albahaca":
            self._product.add("Ingredientes", ingredientes)
        else:
            print("Ingrediente no válido")
            self.ingredientes()

    def coccion(self) -> None:
        coccion = str(input("Elige el método de cocción (horno, parrilla, sartén): "))
        if coccion == "horno" or coccion == "parrilla" or coccion == "sartén":
            self._product.add("Método de cocción", coccion)
        else:
            print("Método de cocción no válido")
            self.coccion()

    def presentacion(self) -> None:
        self._product.add("Detalles de presentación", "Pizza personalizada")

    def maridaje(self) -> None:
        maridaje = str(input("Elige el maridaje (vino tinto, vino blanco, cerveza artesanal): "))
        if maridaje == "vino tinto" or maridaje == "vino blanco" or maridaje == "cerveza artesanal":
            self._product.add("Maridaje", maridaje)
        else:
            print("Maridaje no válido")
            self.maridaje()

    def extra(self) -> None:
        extra = str(input("Elige el extra (aceite de oliva, aceitunas negras, chiles picantes): "))
        if extra == "aceite de oliva" or extra == "aceitunas negras" or extra == "chiles picantes":
            self._product.add("Extra", extra)
        else:
            print("Extra no válido")
            self.extra()

    def precio(self) -> None:
        self._product.add("Precio", 16)


class PizzaPersonalizada():

    def __init__(self) -> None:
        self.parts = {}

    def add(self, category: str, element: str) -> None:
        self.parts[category] = element

    def list_parts(self) -> None:
        print("Pizza parts:")
        for category, element in self.parts.items():
            print(f"{category}: {element}")

    
