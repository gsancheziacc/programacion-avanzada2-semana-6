from abc import ABC, abstractmethod


# Clase Abstracta
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, apellido, rut, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.direccion = direccion

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido

    def set_rut(self, rut):
        self.rut = rut

    def get_rut(self):
        return self.rut

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_direccion(self):
        return self.direccion
