from negocio.entidades.item import Item
from interface_negocio_dados.iRepositorioPedido import IRepositorioPedidos
from negocio.entidades.pedido import Pedido
from utils.exceptions import EstoqueInsuficienteException

class RegistroPedidos:

    def __init__(self, repositorioPedidos: IRepositorioPedidos):
        self.repositorioPedidosMemoria = repositorioPedidos
        pass

    def registroPagamento(self, pedido: Pedido):
        self.repositorioPedidosMemoria.inserirPedido(pedido)
        
