from model.negocio.pagamento.pagamento import Pagamento
from model.negocio.pagamento.pedido import Pedido

from model.negocio.fabricaPagamentoCartao import FabricaPagamentoCartao
from flask import session

class ControladorPagamento:

    def __init__(self):
        self.fabricaPagamentoCartao = FabricaPagamentoCartao()

    def fazPagamento(self,pedido:Pedido, pagamento) -> Pagamento:
        return self.fabricaPagamentoCartao.criaPagamento(pedido=pedido, dadosPagamento=pagamento)
        
