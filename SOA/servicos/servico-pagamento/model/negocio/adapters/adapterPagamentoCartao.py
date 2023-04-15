from model.negocio.pagamento.pagamentoCartao import PagamentoCartao
from model.negocio.pagamento.pagamentoCartaoMockapi import PagamentoCartaoMockapi
from model.negocio.pagamento.pagamento import Pagamento
from model.negocio.pagamento.pedido import Pedido

class AdapterPagamentoCartaoMockapi(PagamentoCartao):
    def __init__(self, pedido, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento):
        super().__init__(pedido, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento)

    def pagar(self):
        mockapi = PagamentoCartaoMockapi()
        dadosPagamentoApi = mockapi.pagar(pedido=self.pedido, numeroCartao=self.numeroCartao, cvv=self.cvv, vencimento=self.vencimento)
        return dadosPagamentoApi
