from abc import ABC, abstractmethod
from datetime import datetime
import csv

class Component(ABC):
    @abstractmethod
    def operacion(self):
        pass


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

class Carpeta(Component):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
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

class Proxy(Component):
    def __init__(self, carpeta: Carpeta) -> None:
        
        self.carpeta = carpeta

    def chequeo_de_contraseña(self, password: str):
        if password == "admin":
            return True
        else:
            return False

    def registro_de_operaciones(self, operacion: str):
        with open("ejercicio2/datos/registro_de_operaciones.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([operacion, datetime.now()])

    def operacion(self, password: str):
        if password == "admin":
            self.carpeta.operacion()
        else:
            print("Contraseña incorrecta")
    
    def crear_documento(self, nombre: str, tamanio: float, tipo: str):
        self.carpeta.add_component(Documento_Component(nombre, tamanio, tipo))

    def crear_enlace(self, nombre: str, tamanio: float, enlace: str):
        self.carpeta.add_component(Enlace_Component(nombre, tamanio, enlace))
    
    def crear_carpeta(self, nombre: str):
        self.carpeta.add_component(Carpeta(nombre))

    def eliminar(self, nombre: str):
        for component in self.carpeta.components:
            if component.decir_nombre() == nombre:
                self.carpeta.remove_component(component)
                break

    def buscar(self, nombre: str):
        for component in self.carpeta.components:
            if component.decir_nombre() == nombre:
                component.operacion()
                break

    def modificar(self, nombre: str, nuevo_nombre: str):
        for component in self.carpeta.components:
            if component.decir_nombre() == nombre:
                component.nombre = nuevo_nombre
                break


if __name__ == "__main__":

    carpeta1 = Carpeta("Carpeta 1")
    carpeta1.add_component(Documento_Component("Documento 1", 10, "docx"))
    carpeta1.add_component(Documento_Component("Documento 2", 20, "docx"))
    carpeta1.add_component(Documento_Component("Documento 3", 30, "docx"))

    proxy = Proxy(carpeta1)
    proxy.operacion("admin")

