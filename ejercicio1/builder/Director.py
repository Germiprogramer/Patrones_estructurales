from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from Pizza import Pizza
from pizzas.Pizza_Barbacoa import PizzaBarbacoa, ConstructorPizzaBarbacoa
from pizzas.Pizza_CuatroQuesos import PizzaCuatroQuesos, ConstructorPizzaCuatroQuesos
from pizzas.Pizza_Hawaiana import PizzaHawaiana, ConstructorPizzaHawaiana
from pizzas.Pizza_Margherita import PizzaMargherita, ConstructorPizzaMargherita
from pizzas.Pizza_Personalizada import PizzaPersonalizada, ConstructorPizzaPersonalizada
from pizzas.Pizza_Infantil import PizzaInfantil, ConstructorPizzaInfantil

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

def to_dict(tipo_de_pizza) -> dict:
    director = Director()
    if tipo_de_pizza == "Pizza Barbacoa":
        builder = ConstructorPizzaBarbacoa()
    elif tipo_de_pizza == "Pizza Cuatro Quesos":
        builder = ConstructorPizzaCuatroQuesos()
    elif tipo_de_pizza == "Pizza Hawaiana":
        builder = ConstructorPizzaHawaiana()
    elif tipo_de_pizza == "Pizza Margherita":
        builder = ConstructorPizzaMargherita()
    elif tipo_de_pizza == "Pizza Personalizada":
        builder = ConstructorPizzaPersonalizada()
    elif tipo_de_pizza == "Pizza Infantil":
        builder = ConstructorPizzaInfantil()
    else:
        print("Tipo de pizza no reconocido")
        return None

    director.builder = builder
    director.build()
    return builder.product.parts

if __name__ == "__main__":

    #pruebame el to_dict

    pizza = to_dict("Pizza Personalizada")
    print(pizza)


    
    


