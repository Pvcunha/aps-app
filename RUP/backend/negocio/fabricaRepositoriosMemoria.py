from IFabricaRepositorios import IFabricaAbstrataRepositorios
from dados.cliente.repositorioClienteMemoria import RepositorioClienteMemoria

class FabricaRepositorios(IFabricaAbstrataRepositorios):

    def criaRepositorioClientesMemoria():
        return RepositorioClienteMemoria()
    