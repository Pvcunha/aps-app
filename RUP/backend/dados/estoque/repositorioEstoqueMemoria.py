from negocio.entidades.item import Item
from interface_negocio_dados.iRepositorioEstoque import IRepositorioEstoque
from utils.utils import SingletonMeta

class RepositorioItemMemoria(IRepositorioEstoque, metaclass=SingletonMeta):

    def __init__(self):
        self.itens = []
        self.id_count = 0
    
    def inserirItem(self, item: Item) -> Item:
        item.id = self.id_count
        self.id_count += 1
        self.itens.append(item)
        return item
    
    def buscarItem(self, email: str) -> Item:
        item = next(iter([c for c in self.itens if c.email == email]))
        if item == None:
            raise Exception("Item nao encontrado")

        return item

    def removerItem(self, email: str) -> Item:
        item = self.buscarItem(email)
        self.itens.pop(Item)
        return item
        

    def atualizarItem(self, email: str, itemAlterado: Item) -> Item:
        item = self.buscarItem(email)
        item = itemAlterado
        return item