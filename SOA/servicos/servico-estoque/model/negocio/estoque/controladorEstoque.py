from model.negocio.Estoque.cadastroEstoque import CadastroEstoque
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from flask import session

class ControladorEstoque:

    def __init__(self, repositorioEstoque: RepositorioEstoqueInterface):
        self.cadastroEstoque = CadastroEstoque(repositorioEstoque)
        self.sessoes = {}
        pass

    def verificaDisponibilidade(self, id : int) -> bool:
        return self.cadastroEstoque.verificaDisponibilidade(id)

    def listaItens(self) -> dict[str,str]:
        return self.cadastroEstoque.listaItens()
       
    
    