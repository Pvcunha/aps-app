from negocio.entidades.cliente import Cliente
from interface_negocio_dados.iRepositorioCliente import IRepositorioClientes
from utils.utils import SingletonMeta

clientes = [Cliente('a', 'b')]

class RepositorioClienteMemoria(IRepositorioClientes, metaclass=SingletonMeta):

    def __init__(self):
        pass
    
    def inserirCliente(self, cliente: Cliente) -> Cliente:
        cliente.id = id_count
        id_count += 1
        clientes.append(cliente)
        return cliente
    
    def buscarCliente(self, email: str) -> Cliente:
        cliente = next(iter([c for c in clientes if c.email == email]))
        if cliente == None:
            raise Exception("Cliente nao encontrado")

        return cliente

    def removerCliente(self, email: str) -> Cliente:
        cliente = self.buscarCliente(email)
        clientes.pop(cliente)
        return cliente
        

    def atualizarCliente(self, email: str, clienteAlterado: Cliente) -> Cliente:
        cliente = self.buscarCliente(email)
        cliente = clienteAlterado
        return cliente

    def getAll(self):
        print(clientes)
        return clientes