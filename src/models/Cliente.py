from src.models.Persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, direccion, mesa):
        super().__init__(nombre, apellido, rut, direccion)
        self.mesa = mesa