from dataclasses import dataclass

@dataclass
class Pedido:
    def __init__(self,id, cliente, itens, status):
        self.id = id
        self.cliente = cliente
        self.itens = itens
        self.status = status
