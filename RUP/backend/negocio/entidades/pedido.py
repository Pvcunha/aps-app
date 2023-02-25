from dataclasses import dataclass

@dataclass
class Pedido:
    def __init__(self,id, client, itens, status):
        self.id = id
        self.cliente = client
        self.itens = itens
        self.status = status
