from abc import ABCMeta, abstractmethod
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface

class FabricaRepositorioInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def criaRepositorioUsuario(self) -> RepositorioUsuariosInterface:
        pass

