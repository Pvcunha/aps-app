from negocio.entidades.pagamentoCartao import PagamentoCartao
from negocio.entidades.pagamentoCartaoMockapi import PagamentoCartaoMockapi
from negocio.entidades.pagamento import Pagamento
from negocio.entidades.pedido import Pedido

class AdapterPagamentoCartaoMockapi(PagamentoCartao):
    def __init__(self, pedido, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento):
        super().__init__(pedido, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento)

    def pagar(self) -> Pagamento:
        mockapi = PagamentoCartaoMockapi()
        dadosPagamentoApi = mockapi.pagar(pedido=self.pedido, numeroCartao=self.numeroCartao, cvv=self.cvv, vencimento=self.vencimento)
        pagamento = PagamentoCartao(self.pedido, self.numeroCartao, self.cvv, self.nomeTitular, self.cpfTitular,self.vencimento)
        return pagamento
