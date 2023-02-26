from negocio.entidades.pedido import Pedido
from backend.interface_negocio_dados.iRepositorioPedido import iRepositorioPedido
from utils import SingletonMeta

class RepositorioPedidoMemoria(iRepositorioPedido, metaclass=SingletonMeta):

    def __init__(self):
        self.Pedidos = []
        self.id_count = 0
    
    def inserirPedido(self, pedido: Pedido) -> Pedido:
        pedido.id = self.id_count
        self.id_count += 1
        self.pedidos.append(pedido)
        return pedido
    
    def buscarPedido(self, email: str) -> Pedido:
        Pedido = next(iter([c for c in self.Pedidos if c.email == email]))
        if Pedido == None:
            raise Exception("Pedido nao encontrado")

        return Pedido

    def removerPedido(self, email: str) -> Pedido:
        Pedido = self.buscarPedido(email)
        self.Pedidos.pop(Pedido)
        return Pedido
        

    def atualizarPedido(self, email: str, pedidoAlterado: Pedido) -> Pedido:
        pedido = self.buscarPedido(email)
        pedido = pedidoAlterado
        return pedido