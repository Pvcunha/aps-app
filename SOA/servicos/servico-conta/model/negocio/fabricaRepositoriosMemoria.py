from model.negocio.iFabricaRepositorios import FabricaRepositorioInterface
from model.dados.iRepositorioUsuarios import RepositorioUsuariosInterface
from model.dados.repositorioUsuarios import RepositorioUsuarioMemoria

class FabricaRepositoriosMemoria(FabricaRepositorioInterface):
    
    def criaRepositorioUsuario(self) -> RepositorioUsuariosInterface:
        return RepositorioUsuarioMemoria()