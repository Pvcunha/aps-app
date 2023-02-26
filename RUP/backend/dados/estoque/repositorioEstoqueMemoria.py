from typing import List
from negocio.entidades.item import Item
from interface_negocio_dados.iRepositorioEstoque import IRepositorioEstoque
from utils.utils import SingletonMeta
from utils.exceptions import EstoqueInsuficienteException
from dados.estoque.estoque_db import Estoque

class RepositorioItemMemoria(IRepositorioEstoque, metaclass=SingletonMeta):

    def __init__(self):
        self.estoque = Estoque()
        self.id_count = 0
    
    def inserirItem(self, item: Item) -> Item:
        item.id = self.id_count
        self.id_count += 1
        self.itens.append(item)
        return item
    
    def buscarItem(self, produtoid: int) -> Item:
        item = next(iter([item for  item in self.estoque.itens if item.produto.id == produtoid]))
        if item == None:
            raise Exception("Item nao encontrado")

        return item

    def removerItem(self, produtoid: int) -> Item:
        item = self.buscarItem(produtoid)
        self.estoque.itens.pop(item)
        return item
        

    def atualizarItem(self, produtoid: int, qtdComprado: int) -> Item:
        item = self.buscarItem(produtoid)
        qtdFinal = item.qtd - qtdComprado
        
        if qtdFinal < 0:
            raise EstoqueInsuficienteException("Nao tem produto sufi")
        
        itemAlterado = Item(produto=item.produto, qtd=qtdFinal)
        self.estoque.itens.pop(item)
        self.estoque.itens.append(itemAlterado)
        return itemAlterado
    
    def getAll(self):
        return self.estoque.itens