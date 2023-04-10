from abc import ABCMeta, abstractmethod
from model.negocio.pedido.pedido import Pedido

class RepositorioPedidosInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def adicionaPedido(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def buscaPedido(self, pedidoID: str) -> Pedido:
        pass
    
    @abstractmethod
    def removePedido(self, pedidoID: str) -> Pedido:
        pass


