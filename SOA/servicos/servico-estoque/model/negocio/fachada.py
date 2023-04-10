from model.negocio.estoque.item import Item
from model.negocio.estoque.controladorEstoque import ControladorEstoque
from model.dados.iRepositorioEstoque import RepositorioEstoqueInterface
from model.negocio.fabricaRepositoriosMemoria import FabricaRepositoriosMemoria
from utils.util import Singleton
from typing import List

class Fachada(metaclass=Singleton):

    def __init__(self, tipoBanco = 'memoria'):
        
        fabricaRepositorios = FabricaRepositoriosMemoria()
        
        repositorioEstoque: RepositorioEstoqueInterface = fabricaRepositorios.criaRepositorioEstoque()
        
        self.controladorEstoque: ControladorEstoque = ControladorEstoque(repositorioEstoque)

    def verificaDisponibilidade(self, item : Item)->Item:
        return self.controladorEstoque.verificaDisponibilidade(item)

    def listaItens(self)->List[Item]:
        return self.controladorEstoque.listaItens()

    def atualizaMenos(self, item : Item)->Item:
        return self.controladorEstoque.atualizaMenos(item)

    def atualizaMais(self, item : Item)->Item:
        return self.controladorEstoque.atualizaMais(item)
pass