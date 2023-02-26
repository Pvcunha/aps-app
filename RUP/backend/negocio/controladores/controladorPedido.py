from negocio.entidades.pedido import Pedido
from negocio.registros.registroPedidos import RegistroPedidos
from utils.utils import Injector, StatusPedido
from fabricas.fabricaPagamentoCartao import FabricaPagamentoCartao
from typing import Dict

class ControladorPedido:

    def __init__(self) -> None:
        injector = Injector()
        self.registroPedidos = RegistroPedidos(injector.repositorioPedidos)
        self.fabricaPagamentoCartao = FabricaPagamentoCartao()

    def fazerPedido(self, pedido, dadosPagamento: Dict) -> Pedido: 

        pedidoFinalizado: Pedido = self.fabricaPagamentoCartao.criaPagamento(pedido=pedido, dadosPagamento=dadosPagamento)
        self.registroPedidos.registroPagamento(pedidoFinalizado)
        