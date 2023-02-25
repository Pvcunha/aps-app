from backend.negocio.iFabricaRepositorios import iFabricaAbstrataRepositorios
from dados.cliente.repositorioClienteMemoria import RepositorioClienteMemoria

class FabricaRepositorios(iFabricaAbstrataRepositorios):

    def criaRepositorioClientesMemoria():
        return RepositorioClienteMemoria()
    