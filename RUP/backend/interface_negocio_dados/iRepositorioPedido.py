from abc import ABCMeta, abstractmethod
from negocio.entidades.pedido import Pedido

class IRepositorioPedidos(metaclass=ABCMeta):
    
    @abstractmethod
    def inserirPedido(self, pedido: Pedido) -> Pedido:
        pass
    
    @abstractmethod
    def buscarPedido(self, email: str) -> Pedido:
        pass

    @abstractmethod
    def removerPedido(self, email: str) -> Pedido:
        pass
        
    @abstractmethod
    def atualizarPedido(self, email: str, pedidoAlterado: Pedido) -> Pedido:
        pass