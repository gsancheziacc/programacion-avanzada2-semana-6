from src.models.Cliente import Cliente

p_cliente = Cliente("Juan", "Pérez", "1-9", "calle siempre viva", "M-28")
s_cliente = Cliente("Felipe", "Rodriguez", "2-7", "por ahí 533", "M-12")
t_cliente = Cliente("Sofia", "Martinez", "3-5", "por allá 190", "M-12")


class Ejemplo:
    def __init__(self, clientes):
        self.clientes = clientes

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.clientes):
            nombre = self.clientes[self.i].get_nombre()
            self.i += 1
            return nombre
        else:
            raise StopIteration


clientes = [p_cliente, s_cliente, t_cliente]
ejemplo_iteracion = Ejemplo(clientes)
iteracion = iter(ejemplo_iteracion)
print(next(iteracion))
print(next(iteracion))
print(next(iteracion))
print(next(iteracion))