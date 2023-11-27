from abc import ABC, abstractmethod
from datetime import datetime
from proxy import Proxy
from composite.carpeta import Carpeta
from composite.documento import Documento_Component

if __name__ == "__main__":

    carpeta1 = Carpeta("Carpeta 1")
    carpeta1.reconstruccion()
    carpeta1.add_component(Documento_Component("Documento 1", 10, "docx"))
    carpeta1.add_component(Documento_Component("Documento 2", 20, "docx"))
    carpeta1.add_component(Documento_Component("Documento 3", 30, "docx"))

    proxy = Proxy(carpeta1)