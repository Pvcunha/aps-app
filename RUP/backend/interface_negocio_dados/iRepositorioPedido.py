from abc import ABCMeta, abstractmethod
from negocio.entidades.pedido import Pedido

class IRepositorioPedidos(metaclass=ABCMeta):
    
    @abstractmethod
    def inserirPedido(self, pedido: Pedido) -> Pedido:
        pass
    
    @abstractmethod
    def buscarPedidos(self, clienteid: str) -> Pedido:
        pass
