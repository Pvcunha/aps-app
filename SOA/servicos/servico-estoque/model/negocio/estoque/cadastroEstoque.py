from model.negocio.estoque.item import Item
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from typing import List

class CadastroEstoque:
    def __init__(self, repositorioEstoque: RepositorioEstoqueInterface):
        self.repositorioEstoque = repositorioEstoque
    pass

    def verificaDisponibilidade(self, item: Item) -> Item:
        item : Item = self.repositorioEstoque.buscarItem(item)

        if item is not None:
            return item
        return None

    def listaItens(self) -> List[Item]:
        lista: list[Item] = self.repositorioEstoque.getAll()
        return lista

    def atualizaMenos(self, item: Item) -> Item:
        item : Item = self.repositorioEstoque.atualizarMenosItem(item)

        if item is not None:
            return item
        return None

    def atualizaMais(self, item: Item) -> Item:
        item : Item = self.repositorioEstoque.atualizarMaisItem(item)

        if item is not None:
            return item
        return None

