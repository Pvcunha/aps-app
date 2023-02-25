from negocio.entidades.cliente import Cliente
from backend.interface_negocio_dados.iRepositorioCliente import IRepositorioCliente

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class RepositorioClienteMemoria(Singleton, IRepositorioCliente):

    def __init__(self):
        self.clientes = []
        self.id_count = 0
    
    def inserirCliente(self, cliente: Cliente) -> Cliente:
        cliente.id = self.id_count
        self.clientes.append(cliente)
        return cliente
    
    def buscarCliente(self, email: str) -> Cliente:
        cliente = next(iter([c for c in self.clientes if c.email == email]))
        if cliente == None:
            raise Exception("Cliente nao encontrado")

        return cliente

    def removerCliente(self, email: str) -> Cliente:
        cliente = self.buscarCliente(email)
        self.clientes.pop(cliente)
        return cliente
        

    def atualizarCliente(self, email: str, clienteAlterado: Cliente) -> Cliente:
        cliente = self.buscarCliente(email)
        cliente = clienteAlterado
        return cliente