from cliente import Cliente

class ControladorLogin:

    def __init__(self, registroClientes) -> None:
        self.registroClientes = registroClientes
    
    def cadastroCliente(self, email, senha):
        clienteNovo = Cliente(email, senha)
        self.registroClientes.adiciona(clienteNovo)