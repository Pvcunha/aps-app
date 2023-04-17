from model.negocio.pagamento.pagamento import Pagamento
from ..pedido.pedido import Pedido
from model.negocio.fabricaPagamentoCartao import FabricaPagamentoCartao

class ControladorPagamento:

    def __init__(self):
        self.fabricaPagamentoCartao = FabricaPagamentoCartao()

    def fazPagamento(self,pedido:Pedido, pagamento) -> Pagamento:
        return self.fabricaPagamentoCartao.criaPagamento(pedido=pedido, dadosPagamento=pagamento)
        
