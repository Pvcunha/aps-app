from interface_negocio_dados.iRepositorioPedido import IRepositorioPedidos
from negocio.entidades.pedido import Pedido
from typing import List

class RegistroPedidos:

    def __init__(self, repositorioPedidos: IRepositorioPedidos):
        self.repositorioPedidos = repositorioPedidos
        

    def registraPedido(self, pedido: Pedido):
        return self.repositorioPedidos.inserirPedido(pedido)
        
    def buscaPedidosdoCliente(self, clienteid) -> List[Pedido]:
        return self.repositorioPedidos.buscarPedidos(clienteid)
