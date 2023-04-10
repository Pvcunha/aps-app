from .iRepositorioPedidosInterface import RepositorioPedidosInterface
from model.negocio.pedido.pedido import Pedido
import uuid

class RepositorioPedidosMemoria(RepositorioPedidosInterface):
    
    def __init__(self):
        self.bancoPedidos = []
    
    def adicionaPedido(self, pedido: Pedido) -> Pedido:
        pedido.id = str(uuid.uuid4())
        self.bancoPedidos.append(pedido)
        print(self.bancoPedidos)
        return pedido
    
    def buscaPedido(self, pedidoID: str) -> Pedido:
        pedido = None
        for p in self.bancoPedidos:
            if p.id == pedidoID:
                return p
        
        raise ValueError('Pedido nao encontrado')
    
    def removePedido(self, pedidoID: str) -> Pedido:
        pedido = self.buscaPedido(pedidoID)
        self.bancoPedidos.remove(pedido)
        return pedido
