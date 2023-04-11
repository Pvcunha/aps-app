from abc import ABC, abstractmethod
from model.negocio.usuario import Usuario

class RepositorioUsuariosInterface(ABC):

    @abstractmethod
    def adicionaUsuario(self, usuario: Usuario):
        pass
    
    @abstractmethod
    def removeUsuario(self, email: str):
        pass

    @abstractmethod
    def buscaUsuario(self, email: str):
        pass

    @abstractmethod
    def pegaTodos(self):
        pass

