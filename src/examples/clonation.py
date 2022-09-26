from src.models.Cliente import Cliente


p_cliente = Cliente("Juan", "Pérez", "1-9", "calle siempre viva", "M-28")
s_cliente = Cliente("Felipe", "Rodriguez", "2-7", "por ahí 533", "M-12")
t_cliente = Cliente("Sofia", "Martinez", "3-5", "por allá 190", "M-12")

c_cliente = p_cliente
print(p_cliente.get_nombre())
print(c_cliente.get_nombre())