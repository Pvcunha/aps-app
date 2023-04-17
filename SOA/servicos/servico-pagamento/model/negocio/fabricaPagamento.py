from typing import Dict
from abc import ABC, abstractmethod
from .pedido.pedido import Pedido
from model.negocio.pagamento.pagamento import Pagamento

class FabricaPagamento(ABC):

    @abstractmethod
    def criaPagamento(pedido: Pedido, dadosPagamento: Dict) -> Pagamento:
        pass