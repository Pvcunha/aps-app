from negocio.entidades.cliente import Cliente
from negocio.registros.registroClientes import RegistroClientes
from utils.utils import myContainer

class ControladorLogin:

    def __init__(self) -> None:
        self.registroClientes = RegistroClientes(myContainer.repositorioClientes)

    def loginCliente(self,email,senha) -> Cliente:
        return self.registroClientes.fazLogin(email, senha)