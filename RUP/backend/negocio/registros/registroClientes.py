from dados.cliente.repositorioClienteMemoria import RepositorioClienteMemoria
from negocio.entidades.cliente import Cliente
from interface_negocio_dados.iRepositorioCliente import IRepositorioClientes
class RegistroClientes:

    def __init__(self, repositorioClientes: IRepositorioClientes):
        self.repositorioCliente = repositorioClientes
        
        self.cliente = None

    def fazLogin(self, email: str, senha: str) -> Cliente:
        cliente = self.repositorioCliente.buscarCliente(email)
        if cliente.senha != senha:
            raise Exception("Senha Incorreta")
        self.cliente = cliente
        return cliente

    def fazCadastro(self, email, senha, cpf) -> Cliente:
        cliente = self.repositorioCliente.inserirCliente(email, senha, cpf)
        return cliente
