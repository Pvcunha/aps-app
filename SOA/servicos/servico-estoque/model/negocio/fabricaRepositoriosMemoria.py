from model.negocio.iFabricaRepositorios import FabricaRepositorioInterface
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from model.dados.repositorioEstoque import RepositorioItemMemoria

class FabricaRepositoriosMemoria(FabricaRepositorioInterface):
    
    def criaRepositorioEstoque(self) -> RepositorioEstoqueInterface:
        return RepositorioItemMemoria()