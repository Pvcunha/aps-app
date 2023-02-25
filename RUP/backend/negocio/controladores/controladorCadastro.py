from negocio.entidades.cliente import Cliente

class ControladorCadastro:

    def __init__(self, registroClientes) -> None:
        self.registroClientes = registroClientes
    
    def cadastroCliente(self, email, senha, cpf, id):
        clienteNovo = Cliente(email, senha, cpf, id)
        self.registroClientes.fazCadastro(clienteNovo)