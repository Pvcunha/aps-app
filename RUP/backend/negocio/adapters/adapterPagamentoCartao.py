from negocio.entidades.pagamentoCartao import PagamentoCartao
from negocio.entidades.pagamentoCartaoMockapi import PagamentoCartaoMockapi

class AdapterPagamentoCartaoMockapi(PagamentoCartao):
    def __init__(self, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento):
        super().__init__(numeroCartao, cvv, nomeTitular, cpfTitular, vencimento)

    def pagar():
        mockapi = PagamentoCartaoMockapi()
        mockapi.pagar()
