#clase usuario simple
class Usuario():
    def __init__(nombre, contrasenia):
        self.nombre = nombre
        self.contrasenia = contrasenia

    #getter y setter
    def get_nombre(self):
        return self.nombre
    
    def get_contrasenia(self):
        return self.contrasenia

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_contrasenia(self, contrasenia):
        self.contrasenia = contrasenia
    
