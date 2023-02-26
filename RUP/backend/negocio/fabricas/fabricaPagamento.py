from typing import Dict
from abc import ABC, abstractmethod
from negocio.entidades.pedido import Pedido
from negocio.entidades.pagamento import Pagamento

class FabricaPagamento(ABC):

    @abstractmethod
    def criaPagamento(pedido: Pedido, dadosPagamento: Dict) -> Pagamento:
        pass