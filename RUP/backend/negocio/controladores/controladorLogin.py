from negocio.entidades.cliente import Cliente


class ControladorLogin:

    def __init__(self,registroClientes) -> None:
        self.registroClientes = registroClientes

    def loginCLiente(self,email,senha) -> Cliente:
        self.registroClientes.fazLogin(email,senha)