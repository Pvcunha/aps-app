from abc import ABCMeta, abstractmethod
from negocio.entidades.cliente import Cliente
class IRepositorioCliente():
    
    @abstractmethod
    def inserirCliente(self, cliente: Cliente) -> Cliente:
        pass
    
    @abstractmethod
    def buscarCliente(self, email: str) -> Cliente:
        pass
    
    @abstractmethod
    def removerCliente(self, email: str) -> Cliente:
        pass
    
    @abstractmethod
    def atualizarCliente(self, email: str) -> Cliente :
        pass