from src.models.Cliente import Cliente
from src.models.Empleado import Empleado

p_cliente = Empleado("Juan", "Pérez", "1-9", "calle siempre viva", "Administrador")
s_cliente = Empleado("Felipe", "Rodriguez", "2-7", "por ahí 533", "Cocinero")
t_cliente = Empleado("Sofia", "Martinez", "3-5", "por allá 190", "Mesero")

c_cliente = p_cliente
print(p_cliente.saludar("asd"))
print(s_cliente.saludar("asd"))
