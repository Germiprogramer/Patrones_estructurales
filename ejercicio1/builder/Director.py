from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from Pizza import Pizza
from Pizza_Barbacoa import PizzaBarbacoa, ConstructorPizzaBarbacoa
from Pizza_CuatroQuesos import PizzaCuatroQuesos, ConstructorPizzaCuatroQuesos
from Pizza_Hawaiana import PizzaHawaiana, ConstructorPizzaHawaiana
from Pizza_Margherita import PizzaMargherita, ConstructorPizzaMargherita
from Pizza_Personalizada import PizzaPersonalizada, ConstructorPizzaPersonalizada

class Director:

        def __init__(self) -> None:
            self._builder = None

        @property
        def builder(self) -> Pizza:
            return self._builder
        
        @builder.setter
        def builder(self, builder: Pizza) -> None:
            """
            The Director works with any builder instance that the client code
            passes to it. This way, the client code may alter the final type of
            the newly assembled product.
            """
            self._builder = builder

        
        def build(self) -> None:
            self.builder.nombre()
            self.builder.masa()
            self.builder.salsa_base()
            self.builder.ingredientes()
            self.builder.coccion()
            self.builder.presentacion()
            self.builder.maridaje()
            self.builder.extra()
            self.builder.precio()

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    director = Director()
    builder = ConstructorPizzaCuatroQuesos()
    director.builder = builder

    
    director.build()

    print(builder.product.parts["Nombre"])


