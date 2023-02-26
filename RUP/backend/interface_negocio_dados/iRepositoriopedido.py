from abc import ABCMeta, abstractmethod
from negocio.entidades.pedido import Pedido

class IRepositorioPedido():
    
    @abstractmethod
    def inserirPedido(self, pedido: Pedido) -> Pedido:
        pass
    
    @abstractmethod
    def buscarPedido(self, id: str) -> Pedido:
        pass
    
    @abstractmethod
    def removerPedido(self, id: str) -> Pedido:
        pass
    
    @abstractmethod
    def atualizarPedido(self, id: str) -> Pedido :
        pass