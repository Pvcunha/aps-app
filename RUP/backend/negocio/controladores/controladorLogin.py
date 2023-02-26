from negocio.entidades.cliente import Cliente
from negocio.registros.registroClientes import RegistroClientes
from utils.utils import Injector

class ControladorLogin:

    def __init__(self) -> None:
        injector = Injector()
        self.registroClientes = RegistroClientes(injector.repositorioClientes)

    def loginCliente(self,email, senha) -> Cliente:
        return self.registroClientes.fazLogin(email, senha)