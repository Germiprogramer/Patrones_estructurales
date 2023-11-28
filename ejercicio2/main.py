from abc import ABC, abstractmethod
from datetime import datetime
from proxy import Proxy
from composite.carpeta import Carpeta
from composite.documento import Documento_Component

if __name__ == "__main__":

    carpeta1 = Carpeta("Carpeta 1")
    # realizamos las operaciones almacenadas en la base de datos para recosntruir la estructura de carpetas
    carpeta1.reconstruccion()
    carpeta1.add_component(Documento_Component("Documento 1", 10, "docx"))
    carpeta1.add_component(Documento_Component("Documento 2", 20, "docx"))
    carpeta1.add_component(Documento_Component("Documento 3", 30, "docx"))
    # creamos un proxy para la carpeta cima
    proxy = Proxy(carpeta1)