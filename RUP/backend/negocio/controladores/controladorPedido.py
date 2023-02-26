from negocio.entidades.pedido import Pedido
from negocio.registros.registroPedidos import RegistroPedidos
from utils.utils import Injector

class ControladorPedido:

    def __init__(self) -> None:
        injector = Injector()
        self.registroPedidos = RegistroPedidos(injector.repositorioPedidos)


    def loginCliente(self,pedido) -> Pedido:

        #fabrica pagamento 

        #if success or not
        self.registroPedidos.registroPagamento(pedido)
        