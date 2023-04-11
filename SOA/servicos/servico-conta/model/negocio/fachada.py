from model.negocio.usuario.usuario import Usuario
from model.negocio.usuario.controladorUsuario import ControladorUsuario
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface
from model.negocio.fabricaRepositoriosMemoria import FabricaRepositoriosMemoria
from utils.util import Singleton

class Fachada(metaclass=Singleton):

    def __init__(self, tipoBanco = 'memoria'):
        
        fabricaRepositorios = FabricaRepositoriosMemoria()
        
        repositorioUsuarios: RepositorioUsuariosInterface = fabricaRepositorios.criaRepositorioUsuario()
        
        self.controladorUsuario: ControladorUsuario = ControladorUsuario(repositorioUsuarios)

    def cadastraUsuario(self, usuario: Usuario) -> Usuario:
        return self.controladorUsuario.cadastraUsuario(usuario)

    def validaLogin(self, usuario: Usuario):
        return self.controladorUsuario.validaLogin(usuario)

    def validaSessao(self, token):
        return self.controladorUsuario.validaSessao(token)
pass