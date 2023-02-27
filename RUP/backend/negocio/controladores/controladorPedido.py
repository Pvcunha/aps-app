from negocio.entidades.pedido import Pedido
from negocio.registros.registroPedidos import RegistroPedidos
from utils.utils import Injector
from negocio.fabricas.fabricaPagamentoCartao import FabricaPagamentoCartao
from negocio.entidades.pagamento import Pagamento
from typing import Dict

class ControladorPedido:

    def __init__(self) -> None:
        injector = Injector()
        self.registroPedidos = RegistroPedidos(injector.repositorioPedidos)
        self.fabricaPagamentoCartao = FabricaPagamentoCartao()

    def fazerPedido(self, pedido: Pedido, dadosPagamento: Dict) -> Pedido: 
        pagamentoFinalizado: Pagamento = self.fabricaPagamentoCartao.criaPagamento(pedido=pedido, dadosPagamento=dadosPagamento)
        pedido = pagamentoFinalizado.pedido
        pedidoRegistrado = self.registroPedidos.registraPedido(pedido)
        return pedidoRegistrado