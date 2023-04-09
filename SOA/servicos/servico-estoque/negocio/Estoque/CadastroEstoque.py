from model.negocio.estoque.item import Item
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface

class CadastroEstoque:
    def __init__(self, repositorioEstoque: RepositorioEstoqueInterface):
        self.repositorioEstoque = repositorioEstoque
    pass

    def verificaDisponibilidade(self, usuario: Usuario) -> Usuario:
        return self.repositorioEstoque.adicionaUsuario(usuario)
    
    def listaItens(self):
        listaItens: list[Item] = self.repositorioEstoque.buscaUsuario(usuario.email) 
        if usuarioBanco.email == usuario.email and usuarioBanco.senha == usuario.senha:
            return usuarioBanco
        else: 
            raise Exception('Senha incorreta')