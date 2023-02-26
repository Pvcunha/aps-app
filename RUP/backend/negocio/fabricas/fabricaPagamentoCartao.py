from typing import Dict
from negocio.fabricas.fabricaPagamento import FabricaPagamento
from negocio.entidades.pedido import Pedido
from negocio.entidades.pagamento import Pagamento
from negocio.adapters.adapterPagamentoCartao import AdapterPagamentoCartao

class FabricaPagamentoCartao(FabricaPagamento):
    
    def criaPagamento(pedido: Pedido, dadosPagamento: Dict) -> Pagamento:
        adapterPagamentoCartao = AdapterPagamentoCartao()