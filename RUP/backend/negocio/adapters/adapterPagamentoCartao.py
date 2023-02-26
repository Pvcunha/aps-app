from negocio.entidades.pagamentoCartao import PagamentoCartao
from negocio.entidades.pagamentoCartaoMockapi import PagamentoCartaoMockapi
from negocio.entidades.pagamento import Pagamento

class AdapterPagamentoCartaoMockapi(PagamentoCartao):
    def __init__(self, pedido, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento):
        super().__init__(pedido, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento)

    def pagar() -> Pagamento:
        mockapi = PagamentoCartaoMockapi()
        dadosPagamentoApi = mockapi.pagar(super().pedido, super().numeroCartao, super().cvv, super().vencimento)
        pagamento = Pagamento(dadosPagamentoApi['Pedido'], dadosPagamentoApi['sucesso'])
        return 
