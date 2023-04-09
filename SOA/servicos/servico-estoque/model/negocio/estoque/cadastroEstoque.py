from model.negocio.estoque.item import Item
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from typing import List

class CadastroEstoque:
    def __init__(self, repositorioEstoque: RepositorioEstoqueInterface):
        self.repositorioEstoque = repositorioEstoque
    pass

    def verificaDisponibilidade(self, item: Item) -> bool:
        item : Item = self.repositorioEstoque.buscarItem(Item)

        if item is not None:
            return True
        return False

    def listaItens(self) -> List[Item]:
        lista: list[Item] = self.repositorioEstoque.getaAll()
        return lista