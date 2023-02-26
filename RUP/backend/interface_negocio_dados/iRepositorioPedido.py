from abc import ABC, abstractmethod
from negocio.entidades.pedido import Pedido

class IRepositorioPedidos:
    
    @abstractmethod
    def inserirPedido(self, pedido: Pedido) -> Pedido:
        pass
    
    @abstractmethod
    def buscarPedidos(self, clienteid: int) -> Pedido:
        pass
