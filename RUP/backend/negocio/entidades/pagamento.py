from abc import ABC, abstractmethod
from negocio.entidades.pedido import Pedido

class Pagamento(ABC):

    def __init__(self, pedido: Pedido):
        self.pedido = pedido

    @abstractmethod
    def pagar(self) -> Pedido:
        pass