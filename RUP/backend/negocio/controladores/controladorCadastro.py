from negocio.entidades.cliente import Cliente
from negocio.registros.registroClientes import RegistroClientes
from utils.utils import Injector

class ControladorCadastro:

    def __init__(self) -> None:
        injector = Injector()
        self.registroClientes = RegistroClientes(injector.repositorioClientes)
    
    def cadastroCliente(self, email, senha, cpf)-> Cliente:
        clienteNovo = Cliente(email, senha, cpf)
        self.registroClientes.fazCadastro(clienteNovo)
        return clienteNovo