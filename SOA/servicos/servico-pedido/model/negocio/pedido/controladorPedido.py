from .pedido import Pedido
from model.dados.iRepositorioPedidosInterface import RepositorioPedidosInterface
from .cadastroPedido import CadastroPedido

import functools
from typing import List, Dict, Union

class ControladorPedido:
    
    def __init__(self, repositorioPedidos: RepositorioPedidosInterface):
        self.cadastroPedidos: CadastroPedido = CadastroPedido(repositorioPedidos)
    
    def criaPedido(self, pedido: Pedido) -> Pedido:
        for produto in pedido.produtos:
            ok = self.verificaDisponibilidade(produto)
            if not ok:
                raise Exception('Produto nao disponivel')
            
        pedido.precoTotal = functools.reduce(lambda x, y: x + y['preco'], pedido.produtos, 0.0)
        return self.cadastroPedidos.criaPedido(pedido)

    def cancelaPedido(self, pedidoID) -> Pedido:
        pedido: Pedido = self.cadastroPedidos.buscaPedido(pedidoID)
        self.__repoeEstoque(pedido.produtos)
        return self.cadastroPedidos.removePedido(pedidoID)

    def confirmaPedido(self, pedidoID: str) -> Pedido:
        pedidoParaConfirmar = self.cadastroPedidos.removePedido(pedidoID)
        pedidoParaConfirmar.status = 'confirmado'
        return self.cadastroPedidos.criaPedido(pedidoParaConfirmar)
    
    def __repoeEstoque(self, produtos: List[Dict[str, Union[str, int]]]):
        #TODO fazer comunicacao com cliente de estoque
        pass

    def verificaDisponibilidade(self, produto):
        # TODO fazer comunicacao com cliente de estoque
        return True
