from model.negocio.usuario import Usuario
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface

class RepositorioUsuarioMemoria(RepositorioUsuariosInterface):

    def __init__(self):
        super().__init__()
        self.usuariosCadastrados = [Usuario(0, "pvc@email.com", "123", "70447872400", 'cliente')]
        self.idCount = 1

    def adicionaUsuario(self, usuario: Usuario):
        #TODO adicionar excecao de email ja cadastrado

        emailList = [u.email for u in self.usuariosCadastrados]
        if usuario.email in emailList:
            raise Exception("Email já cadastrado")
        
        usuario.id = self.idCount
        self.usuariosCadastrados.append(usuario)
        self.idCount += 1
        print(self.usuariosCadastrados)
        return usuario

    def removeUsuario(self, email: str):
        usuario = self.buscaUsuario(email)

        if usuario == None:
            raise Exception("Email não encontrado")
        
        self.usuariosCadastrados.remove(usuario)
        self.idCount -= 1
        return usuario

    def buscaUsuario(self, email: str) -> Usuario:
        usuario = None
        for u in self.usuariosCadastrados:
            if u.email == email:
                usuario = u
        
        if usuario == None:
            raise Exception('Usuario nao encontrado')
        return usuario
    
    def pegaTodos(self):
        return self.usuariosCadastrados

        
