from src.models.Persona import Persona


class Empleado(Persona):
    def __init__(self, nombre, apellido, rut, direccion, cargo):
        super().__init__(nombre, apellido, rut, direccion)
        self.cargo = cargo

    def saludar(self):
        return "Hola, mi nombre es: " + self.get_nombre() + ", Buen día"

    def saludar(self, saludo):
        return "Hola, mi nombre es: " + self.get_nombre() + " " + saludo
