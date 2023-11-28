import sys
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio2\componente.py")
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio2\proxy.py")
from abc import ABC, abstractmethod
from componente import Component
import csv
from composite.documento import Documento_Component
from composite.enlace import Enlace_Component

# Clase Carpeta que implementa la interfaz Component
class Carpeta(Component):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        # Lista para almacenar componentes dentro de la carpeta
        self.components = []
        self.tamanio = 0
    
    def decir_tamanio(self) -> float:
        return self.tamanio

    def decir_nombre(self) -> str:
        return self.nombre

    def operacion(self):
        print(f"Carpeta: {self.nombre}, Tamaño: {self.tamanio}")
        for component in self.components:
            component.operacion()

    def add_component(self, component: Component) -> None:
        self.components.append(component)
        self.tamanio += component.decir_tamanio()


    def remove_component(self, component: Component) -> None:
        self.components.remove(component)
        self.tamanio -= component.decir_tamanio()

    def list_components(self) -> None:
        for component in self.components:
            print(f"\t{component.decir_nombre()}")

    def modificar(self, nombre: str, tamanio: float):
        for component in self.components:
            if component.decir_nombre() == nombre:
                component.tamanio = tamanio
                break

    def acceder_a_carpeta(self, nombre: str):
        for component in self.components:
            if component.decir_nombre() == nombre:
                
                proxy = Proxy(component)
    
     
    # reconstuye la carpeta a partir de un registro de operaciones en un archivo csv
    def reconstruccion(self):
        with open("ejercicio2/datos/registro_de_operaciones.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:

                operacion = row["operacion"]
                fecha = row["fecha"]
                nombre = row["nombre"]
                tamanio = float(row["tamanio"])
                tipo = row["tipo"]
                enlace = row["enlace"]

                if operacion == "crear documento":
                    self.add_component(Documento_Component(nombre, tamanio, tipo))
                elif operacion == "crear enlace":
                    self.add_component(Enlace_Component(nombre, tamanio, enlace))
                elif operacion == "crear carpeta":
                    self.add_component(Carpeta(nombre))
                elif operacion == "eliminar":
                    self.remove_component(nombre)
                elif operacion == "buscar":
                    pass
                elif operacion == "modificar":
                    self.modificar(nombre, tamanio)
                elif operacion == "acceder":
                    pass
                else:
                    print("Operación no válida")

    def list_components(self) -> None:
        for component in self.components:
            print(f"\t{component.decir_nombre()}")