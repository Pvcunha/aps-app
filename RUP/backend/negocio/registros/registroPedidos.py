from interface_negocio_dados.iRepositorioPedido import IRepositorioPedidos
from negocio.entidades.pedido import Pedido
from typing import List

class RegistroPedidos:

    def __init__(self, repositorioPedidos: IRepositorioPedidos):
        self.repositorioPedidosMemoria = repositorioPedidos
        pass

    def registraPedido(self, pedido: Pedido):
        return self.repositorioPedidosMemoria.inserirPedido(pedido)
        
    def buscaPedidosdoCliente(self, clienteid) -> List[Pedido]:
        return self.repositorioPedidosMemoria.buscaPedidos(clienteid)
