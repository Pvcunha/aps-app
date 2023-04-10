from .iFabricaRepositorios import FabricaRepositorioInterface
from model.dados.iRepositorioPedidosInterface import RepositorioPedidosInterface
from model.dados.repositorioPedidosMemoria import RepositorioPedidosMemoria

class FabricaRepositoriosMemoria(FabricaRepositorioInterface):
    
    def criaRepositorioPedidos(self) -> RepositorioPedidosInterface:
        return RepositorioPedidosMemoria()