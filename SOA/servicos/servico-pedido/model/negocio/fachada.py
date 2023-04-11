from .fabricaRepositoriosMemoria import FabricaRepositoriosMemoria
from model.dados.iRepositorioPedidosInterface import RepositorioPedidosInterface
from model.negocio.pedido.pedido import Pedido
from model.negocio.pedido.controladorPedido import ControladorPedido
from utils.util import Singleton

class Fachada(metaclass=Singleton):

    def __init__(self, tipoBanco='memoria'):
        
        if tipoBanco == 'memoria':
            fabricaRepositorios = FabricaRepositoriosMemoria()
        
        repositorioPedidos: RepositorioPedidosInterface = fabricaRepositorios.criaRepositorioPedidos()
        
        self.controladorPedido: ControladorPedido = ControladorPedido(repositorioPedidos)

    def criaPedido(self, pedido: Pedido):
        return self.controladorPedido.criaPedido(pedido)

    def cancelaPedido(self, pedidoID: str) -> Pedido:
        return self.controladorPedido.cancelaPedido(pedidoID)
    
    def confirmaPedido(self, pedidoID: str) -> Pedido:
        return self.controladorPedido.confirmaPedido(pedidoID)
pass