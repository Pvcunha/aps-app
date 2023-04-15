from abc import ABC, abstractmethod
from model.negocio.estoque.item import Item
from typing import List

class RepositorioEstoqueInterface:
    
    @abstractmethod
    def inserirItem(self, item: Item) -> Item:
        pass
    
    @abstractmethod
    def buscarItem(self, itemArg: Item) -> Item:
        pass
    
    @abstractmethod
    def removerItem(self, produtoid: int) -> Item:
        pass
    
    @abstractmethod
    def atualizarItem(self, produtoid: int, qtd: int) -> Item :
        pass
    @abstractmethod
    def atualizarMenosItem(self, itemArg:Item) -> Item:
        pass
    @abstractmethod
    def atualizarMaisItem(self, itemArg:Item) -> Item:
        pass
    @abstractmethod
    def getAll(self) -> List[Item]:
        pass