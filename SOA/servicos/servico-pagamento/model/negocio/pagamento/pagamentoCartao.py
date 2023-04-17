from model.negocio.pagamento.pagamento import Pagamento
from ..pedido.pedido import Pedido

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