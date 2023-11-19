from __future__ import annotations
from abc import ABC, abstractmethod


class Pizza(ABC):
   
    """
    La interfaz Builder especifica métodos para crear las diferentes partes de los objetos Producto.
    """

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass
    
    @abstractmethod
    def nombre(self) -> None:
        pass

    @abstractmethod
    def masa(self) -> None:
        pass

    @abstractmethod
    def salsa_base(self) -> None:
        pass

    @abstractmethod
    def ingredientes(self) -> None:
        pass

    @abstractmethod
    def coccion(self) -> None:
        pass

    @abstractmethod
    def presentacion(self) -> None:
        pass

    @abstractmethod
    def maridaje(self) -> None:
        pass

    @abstractmethod
    def extra(self) -> None:
        pass

    @abstractmethod
    def precio(self) -> None:
        pass