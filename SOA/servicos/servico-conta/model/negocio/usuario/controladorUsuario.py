from model.negocio.usuario.usuario import Usuario
from model.negocio.usuario.cadastroUsuarios import CadastroUsuarios
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface

class ControladorUsuario:

    def __init__(self, repositorioUsuarios: RepositorioUsuariosInterface):
        self.cadastroUsuarios = CadastroUsuarios(repositorioUsuarios)
        pass

    def cadastraUsuario(self, usuario: Usuario) -> Usuario:
        return self.cadastroUsuarios.cadastraUsuario(usuario)

    def validaLogin(self, usuario: Usuario):
        pass