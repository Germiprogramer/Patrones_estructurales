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

    def modificar(self, nombre: str, tamanio: float):
        for component in self.components:
            if component.decir_nombre() == nombre:
                component.tamanio = tamanio
                break

    def acceder_a_carpeta(self, nombre: str):
        #haz que se pueda acceder a una carpeta y que la carpeta que se acceda sea la carpeta cima
        for component in self.components:
            if component.decir_nombre() == nombre:
                
                proxy = Proxy(component)

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
                    self.add_component(Carpeta(nombre, None))
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

class Proxy(Component):
    def __init__(self, carpeta: Carpeta) -> None:

        self.carpeta = carpeta
        self.acceso()

    def acceso(self):
        nombre = input("Ingrese el nombre de usuario: ")
        # buscame el usuario en la base de datos usuario en funcion de su nombre
        with open("ejercicio2/datos/usuarios.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'contrasenia' in row and row['nombre'] == nombre:
                    contrasenia = row['contrasenia']
                    entrada_contrasenia = input("Ingrese la contraseña: ")
                    if contrasenia == entrada_contrasenia:
                        print("Contraseña correcta")
                        self.operacion()
                    else:
                        print("Contraseña incorrecta")
                        self.acceso()
                else:
                    print("Usuario no encontrado")
                    self.acceso()
            

if __name__ == "__main__":

    carpeta1 = Carpeta("Carpeta 1")
    carpeta1.reconstruccion()
    carpeta1.add_component(Documento_Component("Documento 1", 10, "docx"))
    carpeta1.add_component(Documento_Component("Documento 2", 20, "docx"))
    carpeta1.add_component(Documento_Component("Documento 3", 30, "docx"))

    proxy = Proxy(carpeta1)
    

