from componente import Component
from datetime import datetime
import csv
from composite.documento import Documento_Component
from composite.enlace import Enlace_Component
from composite.carpeta import Carpeta
from usuario import Usuario

class Proxy(Component):
    def __init__(self, carpeta: Carpeta) -> None:

        self.carpeta = carpeta
        self.acceso()

    def acceso(self):
        nombre = input("Ingrese el nombre de usuario: ")
        # buscar el usuario en la base de datos usuario en funcion de su nombre
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

        


    def registro_de_operaciones(self, operacion: str, nombre, tamanio, tipo, enlace):
        # registrar la operacion en la base de datos
        with open("ejercicio2/datos/registro_de_operaciones.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([operacion, datetime.now(), nombre, tamanio, tipo, enlace])


    def operacion(self):
        # solicitar la operacion que se desea realizar
        operacion = input("Ingrese la operación que desea realizar: ")
        nombre = None
        tamanio = 0
        tipo = "No aplica"
        enlace = "No aplica"
        if operacion == "crear documento":
            nombre = input("Ingrese el nombre del documento: ")
            tamanio = float(input("Ingrese el tamaño del documento: "))
            tipo = input("Ingrese el tipo del documento: ")
            self.crear_documento(nombre, tamanio, tipo)
        elif operacion == "crear enlace":
            nombre = input("Ingrese el nombre del enlace: ")
            tamanio = 0
            enlace = input("Ingrese el enlace: ")
            self.crear_enlace(nombre, tamanio, enlace)
        elif operacion == "crear carpeta":
            nombre = input("Ingrese el nombre de la carpeta: ")
            self.crear_carpeta(nombre)
        elif operacion == "eliminar":
            nombre = input("Ingrese el nombre del componente que desea eliminar: ")
            self.eliminar(nombre)
        elif operacion == "buscar":
            nombre = input("Ingrese el nombre del componente que desea buscar: ")
            self.buscar(nombre)
        elif operacion == "modificar":
            nombre = input("Ingrese el nombre del componente que desea modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del componente: ")
            self.modificar(nombre, nuevo_nombre)
        elif operacion == "acceder":
            nombre = input("Ingrese el nombre de la carpeta a la que desea acceder: ")
            self.acceder_a_carpeta(nombre)
        elif operacion = "decir tamanio":
            self.decir_tamanio()
        else:
            print("Operación no válida")
        self.registro_de_operaciones(operacion, nombre, tamanio, tipo, enlace)
    
    def crear_documento(self, nombre: str, tamanio: float, tipo: str):
        # crear un documento y agregarlo a la carpeta
        self.carpeta.add_component(Documento_Component(nombre, tamanio, tipo))

    def crear_enlace(self, nombre: str, tamanio: float, enlace: str):
        # crear un enlace y agregarlo a la carpeta
        self.carpeta.add_component(Enlace_Component(nombre, tamanio, enlace))
    
    def crear_carpeta(self, nombre: str):
        # crear una carpeta y agregarla a la carpeta
        self.carpeta.add_component(Carpeta(nombre))

    def eliminar(self, nombre: str):
        # eliminar un componente de la carpeta
        for component in self.carpeta.components:
            if component.decir_nombre() == nombre:
                self.carpeta.remove_component(component)
                break

    def buscar(self, nombre: str):
        # buscar un componente de la carpeta
        for component in self.carpeta.components:
            if component.decir_nombre() == nombre:
                component.operacion()
                break

    def modificar(self, nombre: str, nuevo_nombre: str):
        # modificar el nombre de un componente de la carpeta
        for component in self.carpeta.components:
            if component.decir_nombre() == nombre:
                component.nombre = nuevo_nombre
                break
    
    def acceder_a_carpeta(self, nombre: str):
        #haz que se pueda acceder a una carpeta y que la carpeta que se acceda sea la carpeta cima
        for component in self.carpeta.components:
            print(component.decir_nombre())
            if component.decir_nombre() == nombre:          
                proxy = Proxy(component)
    
    def decir_tamanio(self):
        # decir el tamaño de la carpeta
        print(self.carpeta.decir_tamanio())