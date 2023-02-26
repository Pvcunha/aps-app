from abc import ABC, ABCMeta, abstractmethod
from interface_negocio_dados.iRepositorioCliente import IRepositorioClientes
from interface_negocio_dados.iRepositorioEstoque import IRepositorioEstoque
from interface_negocio_dados.iRepositorioPedido import IRepositorioPedidos

class IFabricaAbstrataRepositorios(metaclass=ABCMeta):
    
    @abstractmethod
    def criaRepositorioClientes(self) -> IRepositorioClientes:
        pass
    
    @abstractmethod
    def criaRepositorioEstoque(self) -> IRepositorioEstoque:
        pass

    def criaRepositorioPedido(self) -> IRepositorioPedidos:
        pass