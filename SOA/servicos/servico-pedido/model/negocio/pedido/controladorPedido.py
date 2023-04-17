from .pedido import Pedido
from model.dados.iRepositorioPedidosInterface import RepositorioPedidosInterface
from .cadastroPedido import CadastroPedido
from middlewares.fronteiraEstoque import FronteiraEstoque

import functools
from typing import List, Dict, Union
import uuid

class ControladorPedido:
    
    def __init__(self, repositorioPedidos: RepositorioPedidosInterface):
        self.cadastroPedidos: CadastroPedido = CadastroPedido(repositorioPedidos)
    
    def criaPedido(self, pedido: Pedido) -> Pedido:
        for produto in pedido.produtos:
            ok = self.__verificaDisponibilidade(produto)
            if not ok:
                raise Exception('Produto nao disponivel')
            
        pedido.precoTotal = functools.reduce(lambda x, y: x + y['valor']*y['qtd'], pedido.produtos, 0.0)
        
        ok = self.__removeEstoque(pedido.produtos)
        if not ok:
            raise Exception('Erro ao remover pedidos')
        
        pedido.id = str(uuid.uuid4())

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
        return FronteiraEstoque.alterarEstoque(produtos=produtos, rota='/atualizaMaisPedido')
    
    def __removeEstoque(self, produtos: List[Dict[str, Union[str, int]]]):
        return FronteiraEstoque.alterarEstoque(produtos=produtos, rota='/atualizaMenosPedido')

    def __verificaDisponibilidade(self, produto):
        return FronteiraEstoque.verificaDisponibilidade(produto)
