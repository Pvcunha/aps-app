from interface_negocio_dados.iFabricaRepositorios import IFabricaAbstrataRepositorios
from dados.cliente.repositorioClienteMemoria import RepositorioClienteMemoria
from interface_negocio_dados.iRepositorioCliente import IRepositorioClientes
from dados.cliente.repositorioClienteMemoria import RepositorioClienteMemoria
from dados.estoque.repositorioEstoqueMemoria import RepositorioItemMemoria
from interface_negocio_dados.iRepositorioEstoque import IRepositorioEstoque
from interface_negocio_dados.iRepositorioPedido import IRepositorioPedidos

class FabricaRepositoriosMemoria(IFabricaAbstrataRepositorios):

    def criaRepositorioClientes(self) -> IRepositorioClientes:
        return RepositorioClienteMemoria()
    
    def criaRepositorioEstoque(self) -> IRepositorioEstoque:
        return RepositorioItemMemoria()

    def criaRepositorioPedido(self) -> IRepositorioPedidos:
        pass
    
