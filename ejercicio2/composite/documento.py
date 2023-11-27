import sys
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio2\componente.py")
from abc import ABC, abstractmethod
from componente import Component

class Documento_Component(Component):
    def __init__(self, nombre: str, tamanio: float, tipo: str) -> None:
        self.nombre = nombre
        self.tamanio = tamanio
        self.tipo = tipo
        self.contenido = None
    
    def decir_tamanio(self) -> float:
        return self.tamanio

    def decir_nombre(self) -> str:
        return self.nombre

    def operacion(self):
        print(f"Documento: {self.nombre}, Tamaño: {self.tamanio}, Tipo: {self.tipo}")

