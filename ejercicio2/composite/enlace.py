import sys
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio2\componente.py")
from abc import ABC, abstractmethod
from componente import Component

class Enlace_Component(Component):
    def __init__(self, nombre: str, tamanio: float, enlace: str) -> None:
        self.nombre = nombre
        self.tamanio = tamanio
        self.enlace = enlace
    
    def decir_tamanio(self) -> float:
        return self.tamanio

    def decir_nombre(self) -> str:
        return self.nombre

    def operacion(self):
        print(f"Enlace: {self.nombre}, Tamaño: {self.tamanio}, Enlace: {self.enlace}")
