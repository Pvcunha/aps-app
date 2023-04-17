from typing import List
from model.negocio.estoque.item import Item
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from utils.exceptions import EstoqueInsuficienteException
from model.dados.estoque_db import Estoque

class RepositorioItemMemoria(RepositorioEstoqueInterface):

    def __init__(self):
        self.estoque = Estoque()
        self.id_count = 0
    
    def inserirItem(self, item: Item) -> Item:
        item.id = self.id_count
        self.id_count += 1
        self.itens.append(item)
        return item
    
    def buscarItem(self, itemArg: Item) -> Item:
        print(type(itemArg))
        for item in self.estoque.itens:
            print(item.produto.id)
        try:
            item = next(iter([item for  item in self.estoque.itens if item.produto.id == itemArg.produto.id]))

            return item
        except StopIteration:
            print("NAO ACHOOU")
            raise Exception("ID NAO ENCONTRADO")


    def removerItem(self, produtoid: int) -> Item:
        item = self.buscarItem(produtoid)
        self.estoque.itens.pop(item)
        return item
        

    def atualizarMenosItem(self, itemArg:Item) -> Item:
        item = self.buscarItem(itemArg)
        qtdFinal = item.qtd - itemArg.qtd
        
        if qtdFinal < 0:
            raise EstoqueInsuficienteException("Nao tem produto sufi")
        
        item.qtd = qtdFinal
        return item

    def atualizarMaisItem(self, itemArg:Item) -> Item:
        item = self.buscarItem(itemArg)
        print("DEBUGAAA")
        print(type(item))
        print(type(itemArg))
        qtdFinal = item.qtd + itemArg.qtd
        
        item.qtd = qtdFinal
        return item
        
    
    
    def getAll(self):
        return self.estoque.itens