from model.negocio.usuario.usuario import Usuario
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface

class CadastroUsuarios:
    def __init__(self, repositorioUsuarios: RepositorioUsuariosInterface):
        self.repositorioUsuarios = repositorioUsuarios
    pass

    def cadastraUsuario(self, usuario: Usuario) -> Usuario:
        return self.repositorioUsuarios.adicionaUsuario(usuario)