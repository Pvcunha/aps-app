from abc import ABCMeta, abstractmethod
from negocio.entidades.item import Item
class IRepositorioEstoque():
    
    @abstractmethod
    def inserirItem(self, item: Item) -> Item:
        pass
    
    @abstractmethod
    def buscarItem(self, email: str) -> Item:
        pass
    
    @abstractmethod
    def removerItem(self, email: str) -> Item:
        pass
    
    @abstractmethod
    def atualizarItem(self, email: str) -> Item :
        pass