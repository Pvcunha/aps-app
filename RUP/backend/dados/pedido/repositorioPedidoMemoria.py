from negocio.entidades.pedido import Pedido
from backend.interface_negocio_dados.iRepositorioPedido import iRepositorioPedido
from utils import SingletonMeta
from typing import List

class RepositorioPedidoMemoria(iRepositorioPedido, metaclass=SingletonMeta):

    def __init__(self):
        self.pedidos: List[Pedido] = []
        self.id_count = 0
    
    def inserirPedido(self, pedido: Pedido) -> Pedido:
        pedido.id = self.id_count
        self.id_count += 1
        self.pedidos.append(pedido)
        return pedido
    
    def buscarPedidos(self, clienteid) -> List[Pedido]:
        return [pedido for pedido in self.pedidos if pedido.clienteId == clienteid]
    