from model.negocio.estoque.cadastroEstoque import CadastroEstoque
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from model.negocio.estoque.item import Item
from typing import List

class ControladorEstoque:

    def __init__(self, repositorioEstoque: RepositorioEstoqueInterface):
        self.cadastroEstoque = CadastroEstoque(repositorioEstoque)
        self.sessoes = {}
        pass

    def verificaDisponibilidade(self, item : Item) -> bool:
        return self.cadastroEstoque.verificaDisponibilidade(id)

    def listaItens(self) -> List[Item]:
        return self.cadastroEstoque.listaItens()
       
    
    