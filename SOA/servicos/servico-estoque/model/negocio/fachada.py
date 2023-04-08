from model.negocio.Estoque.item import Item
from model.negocio.Estoque.controladorEstoque import ControladorEstoque
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from model.negocio.fabricaRepositoriosMemoria import FabricaRepositoriosMemoria
from utils.util import Singleton

class Fachada(metaclass=Singleton):

    def __init__(self, tipoBanco = 'memoria'):
        
        fabricaRepositorios = FabricaRepositoriosMemoria()
        
        repositorioEstoque: RepositorioEstoqueInterface = fabricaRepositorios.criaRepositorioEstoque()
        
        self.controladorEstoque: ControladorEstoque = ControladorEstoque(repositorioEstoque)

    def verificaDisponibilidade(self, produtoId: int, qtdInteresse: int)->bool:
        return self.controladorEstoque.verificaDisponibilidade(produtoId,qtdInteresse)

    def listaItens(self)->List[Item]:
        return self.controladorEstoque.listaItens()
pass