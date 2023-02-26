from negocio.entidades.pagamento import Pagamento
from negocio.entidades.pedido import Pedido

class PagamentoCartao(Pagamento):
    
    def __init__(self, pedido, numeroCartao, cvv, nomeTitular, cpfTitular, vencimento):
        super().__init__(pedido)
        self.numeroCartao = numeroCartao
        self.cvv = cvv
        self.nomeTitular = nomeTitular
        self.cpfTitular = cpfTitular
        self.vencimento = vencimento

    def pagar(self) -> Pedido:
        pass