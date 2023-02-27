from typing import Dict
from negocio.fabricas.fabricaPagamento import FabricaPagamento
from negocio.entidades.pedido import Pedido
from negocio.entidades.pagamento import Pagamento

class FabricaPagamentoPaypal(FabricaPagamento):

    def criaPagamento(pedido: Pedido, dadosPagamento: Dict) -> Pagamento:
        #TODO cria pagamento paypal
        pass