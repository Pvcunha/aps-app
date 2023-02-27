from negocio.entidades.cliente import Cliente
from negocio.registros.registroClientes import RegistroClientes
from utils.utils import Injector

class ControladorCadastro:

    def __init__(self) -> None:
        injector = Injector()
        self.registroClientes = RegistroClientes(injector.repositorioClientes)
    
    def cadastroCliente(self, email, senha, cpf)-> Cliente:
        clienteNovo = self.registroClientes.fazCadastro(email, senha, cpf)
        return clienteNovo