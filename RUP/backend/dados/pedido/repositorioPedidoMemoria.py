from negocio.entidades.pedido import Pedido
from interface_negocio_dados.iRepositorioPedido import IRepositorioPedidos
from utils.utils import SingletonMeta
from typing import List

class RepositorioPedidoMemoria(IRepositorioPedidos, metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.pedidos = []
        self.idcount = 0
    
    def inserirPedido(self, pedido: Pedido) -> Pedido:
        pedidoNovo = Pedido(self.idcount, pedido.clienteId, pedido.valor, pedido.itens, pedido.status)
        self.pedidos.append(pedidoNovo)
        self.idcount += 1
        return pedidoNovo

    def buscarPedidos(self, clienteid: int) -> Pedido:
        pedidos = [pedido for pedido in self.pedidos if pedido.clienteid == clienteid]
        return pedidos