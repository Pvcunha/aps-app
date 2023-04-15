from model.negocio.pagamento.controladorPagamento import ControladorPagamento
from utils.util import Singleton

class Fachada(metaclass=Singleton):

    def __init__(self, tipoBanco = 'memoria'):

        self.controladorPagamento: ControladorPagamento = ControladorPagamento(repositorioPagamentos)

    def fazPagamento(self,pedido, dadosPagamento):
        return self.controladorPagamento.fazPagamento(pedido,dadosPagamento)

pass