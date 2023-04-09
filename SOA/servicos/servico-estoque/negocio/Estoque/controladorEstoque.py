from model.negocio.estoque.cadastroEstoque import CadastroEstoque
from model.negocio.estoque.item import Item
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from flask import session

class ControladorEstoque:

    def __init__(self, repositorioEstoque: RepositorioEstoqueInterface):
        self.cadastroEstoque = CadastroEstoque(repositorioEstoque)
        pass

    def verificaDisponibilidade(self, id : int, qtd : int) -> bool:
        return self.cadastroEstoque.verificaDisponibilidade(id,qtd)

    def listaItens(self) -> list[Item]:
        return self.cadastroEstoque.listaItens()
       
    
    