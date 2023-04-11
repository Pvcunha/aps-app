from model.negocio.usuario.usuario import Usuario
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface

class CadastroUsuarios:
    def __init__(self, repositorioUsuarios: RepositorioUsuariosInterface):
        self.repositorioUsuarios = repositorioUsuarios
    pass

    def cadastraUsuario(self, usuario: Usuario) -> Usuario:
        return self.repositorioUsuarios.adicionaUsuario(usuario)
    
    def validaLogin(self, usuario: Usuario) -> Usuario:
        # TODO adicionar exception de senha incorreta
        usuarioBanco: Usuario = self.repositorioUsuarios.buscaUsuario(usuario.email) 
        if usuarioBanco.email == usuario.email and usuarioBanco.senha == usuario.senha:
            return usuarioBanco
        else: 
            raise Exception('Senha incorreta')