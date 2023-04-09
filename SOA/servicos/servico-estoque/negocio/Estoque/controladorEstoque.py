from model.negocio.estoque.cadastroEstoque import CadastroEstoque
from model.negocio.estoque.item import Item
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from flask import session
from typing import List


class ControladorEstoque:

    def __init__(self, repositorioEstoque: RepositorioEstoqueInterface):
        self.cadastroEstoque = CadastroEstoque(repositorioEstoque)
        pass

    def verificaDisponibilidade(self, id : int, qtd : int) -> bool:
        return self.cadastroEstoque.verificaDisponibilidade(id,qtd)

    def listaItens(self) -> List[Item]:
        return self.cadastroEstoque.listaItens()
       
    
    