from model.negocio.usuario.usuario import Usuario
from model.negocio.usuario.cadastroUsuarios import CadastroUsuarios
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface
from flask import session

class ControladorUsuario:

    def __init__(self, repositorioUsuarios: RepositorioUsuariosInterface):
        self.cadastroUsuarios = CadastroUsuarios(repositorioUsuarios)
        self.sessoes = {}
        pass

    def cadastraUsuario(self, usuario: Usuario) -> Usuario:
        return self.cadastroUsuarios.cadastraUsuario(usuario)

    def validaLogin(self, usuario: Usuario) -> Usuario:
        usuario = self.cadastroUsuarios.validaLogin(usuario)
        self._registraSessao(usuario)
        return usuario
    
    def _registraSessao(self, usuario: Usuario):
        self.sessoes[usuario.id] = usuario.email 

    def validaSessao(self, token):
        if int(token['id']) not in self.sessoes.keys():
            raise Exception('Usuario nao esta logado')
        
        return token
