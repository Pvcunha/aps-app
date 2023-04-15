from abc import ABCMeta, abstractmethod
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface

class FabricaRepositorioInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def criaRepositorioEstoque(self) -> RepositorioEstoqueInterface:
        pass

