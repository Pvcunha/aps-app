from model.dados.iRepositorioPedidosInterface import RepositorioPedidosInterface
from model.negocio.pedido.pedido import Pedido

class CadastroPedido:

    def __init__(self, repositorioPedidos: RepositorioPedidosInterface):
        self.repositorioPedidos = repositorioPedidos
    
    def criaPedido(self, pedido: Pedido):
        return self.repositorioPedidos.adicionaPedido(pedido)
    
    def buscaPedido(self, pedidoID: str):
        return self.repositorioPedidos.buscaPedido(pedidoID)
    
    def removePedido(self, pedidoID: str):
        return self.repositorioPedidos.removePedido(pedidoID)