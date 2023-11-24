from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod
import sys
# insertamos la ruta donde se encuentra el directorio de builder
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\builder")
from Pizza import Pizza

class ConstructorPizzaPersonalizada(Pizza):

    def __init__(self, nombre, masa, salsa_base, ingredientes, coccion, presentacion, maridaje, extra) -> None:
        self.nombre_pizza = nombre
        self.masa_pizza = masa
        self.salsa_base_pizza = salsa_base
        self.ingredientes_pizza = ingredientes
        self.coccion_pizza = coccion
        self.presentacion_pizza = presentacion
        self.maridaje_pizza = maridaje
        self.extra_pizza = extra
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
        
        self._product.add("Nombre", self.nombre_pizza)
        

    def masa(self) -> None:
        masa = self.masa_pizza
        if masa == "fina" or masa == "normal" or masa == "gruesa":
            self._product.add("Masa", masa)
        else:
            self._product.add("Masa", "masa base")
            
        

    def salsa_base(self) -> None:
        salsa = self.salsa_base_pizza
        if salsa == "tomate" or salsa == "barbacoa" or salsa == "pesto":
            self._product.add("Salsa", salsa)
        else:
            self._product.add("Salsa", "ninguna")
            
    #queda por corregir esta funcion
    def ingredientes(self) -> None:
        ingredientes = self.ingredientes_pizza
        if ingredientes == "queso" or ingredientes == "jamón" or ingredientes == "piña" or ingredientes == "pollo" or ingredientes == "cebolla" or ingredientes == "cilantro" or ingredientes == "chiles" or ingredientes == "aceitunas" or ingredientes == "albahaca":
            self._product.add("Ingredientes", ingredientes)
        else:
            self._product.add("Ingredientes", "ninguno")
            print("Ingrediente no válido")
            

    def coccion(self) -> None:
        coccion = self.coccion_pizza
        if coccion == "horno" or coccion == "parrilla" or coccion == "sartén":
            self._product.add("Método de cocción", coccion)
        else:
            self._product.add("Método de cocción", "horno")
            

    def presentacion(self) -> None:
        self._product.add("Detalles de presentación", "Pizza personalizada")

    def maridaje(self) -> None:
        maridaje = self.maridaje_pizza
        if maridaje == "vino tinto" or maridaje == "vino blanco" or maridaje == "cerveza artesanal":
            self._product.add("Maridaje", maridaje)
        else:
            self._product.add("Maridaje", "ninguno")
            

    def extra(self) -> None:
        extra = self.extra_pizza
        if extra == "aceite de oliva" or extra == "aceitunas negras" or extra == "chiles picantes":
            self._product.add("Extra", extra)
        else:
            self._product.add("Extra", "ninguno")

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

    
