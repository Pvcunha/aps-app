from negocio.entidades.cliente import Cliente
from interface_negocio_dados.iRepositorioCliente import IRepositorioClientes
from utils.utils import SingletonMeta
from dados.cliente.clientes_db import clientesDB

class RepositorioClienteMemoria(IRepositorioClientes, metaclass=SingletonMeta):

    def __init__(self):
        pass
    
    def inserirCliente(self, email: str, senha: str, cpf: str) -> Cliente:
        id = clientesDB.id_count
        clientesDB.id_count += 1
        clienteNovo = Cliente(email, senha, cpf, id)
        clientesDB.clientesappend(clienteNovo)
        return clienteNovo
    
    def buscarCliente(self, email: str) -> Cliente:
        cliente = next(iter([c for c in clientesDB.clientes if c.email == email]))
        if cliente == None:
            raise Exception("Cliente nao encontrado")

        return cliente

    def removerCliente(self, email: str) -> Cliente:
        cliente = self.buscarCliente(email)
        clientesDB.pop(cliente)
        return cliente
        

    def atualizarCliente(self, email: str, clienteAlterado: Cliente) -> Cliente:
        cliente = self.buscarCliente(email)
        cliente = clienteAlterado
        return cliente

    def getAll(self):
        return clientesDB.clientes