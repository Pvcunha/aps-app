from abc import ABCMeta, abstractmethod
from model.dados.iRepositorioPedidosInterface import RepositorioPedidosInterface

class FabricaRepositorioInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def criaRepositorioPedidos(self) -> RepositorioPedidosInterface:
        pass

