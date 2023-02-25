from dados.cliente.repositorioClienteMemoria import RepositorioClienteMemoria
from negocio.entidades.cliente import Cliente

class RegistroCliente:

    def __init__(self):
        self.repositorioClienteMemoria = RepositorioClienteMemoria()
        
    def fazLogin(self, email: str, senha: str) -> Cliente:
        cliente = self.repositorioClienteMemoria.buscarCliente(email)
        if cliente.senha != senha:
            raise Exception("Senha Incorreta")
        return cliente

    def fazCadastro(self, cliente: Cliente) -> Cliente:
        cliente = self.repositorioClienteMemoria.inserirCliente(cliente)
        return cliente
