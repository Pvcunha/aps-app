from flask import jsonify, Response
from utils.utils import SingletonMeta, Injector, CustomJSONEncoder
from utils.exceptions import EstoqueInsuficienteException
from negocio.controladores.controladorLogin import ControladorLogin
from negocio.controladores.controladorCadastro import ControladorCadastro
from negocio.controladores.controladorEstoque import ControladorEstoque
from negocio.controladores.controladorPedido import ControladorPedido
from negocio.fabricas.fabricaRepositoriosMemoria import FabricaRepositoriosMemoria

class Fachada(metaclass=SingletonMeta):
    
    def __init__(self, db_type: str='padrao'):
        if db_type == 'padrao':
            self.__fabricaRepositorio = FabricaRepositoriosMemoria()
        else:
            pass

        repositorioClientes = self.__fabricaRepositorio.criaRepositorioClientes()
        repositorioEstoque = self.__fabricaRepositorio.criaRepositorioEstoque()
        repositorioPedidos = self.__fabricaRepositorio.criaRepositorioPedido()
        
        myContainer = Injector()
        myContainer.repositorioClientes = repositorioClientes
        myContainer.repositorioEstoque = repositorioEstoque
        myContainer.repositorioPedidos = repositorioPedidos
        
        self.__controladorLogin = ControladorLogin()
        self.__controladorCadastro = ControladorCadastro()
        self.__controladorEstoque = ControladorEstoque()
        self.__controladorPedido = ControladorPedido()

    def fazLogin(self, email: str, senha: str) -> Response:
        try:
            cliente = self.__controladorLogin.loginCliente(email, senha)
            token = "logged"
            response = jsonify({'cliente': cliente.__dict__, 'token': token})
            response.status_code = 200
            return response
        except Exception as err:
            print(err)
            return Response(status=204)

    def fazCadastro(self, email: str, senha: str, cpf: str) -> Response:
        try:
            cliente = self.__controladorCadastro.cadastroCliente(email, senha, cpf)
            response = jsonify(cliente.__dict__)
            response.status_code = 200
            return response
        except Exception as err:
            print(err)
            return Response(status=400)
    
    def verificaDisponibilidade(self, produtoid: int, qtdInteresse: int):
        # mudar na arquitetura de adicionarAoCarrinho para verificarDisponibilidade
        try:
            item = self.__controladorEstoque.verificaDisponibilidade(produtoid, qtdInteresse)
            response = jsonify(item.__dict__)
            response.status_code = 200
            return response
        except EstoqueInsuficienteException as err:
            return Response(err.message, status=400)
    
    def listaItens(self):
        itens = self.__controladorEstoque.pegaEstoque()
        itens_dicts = [item.__dict__ for item in itens]
        return jsonify(itens_dicts)

    def fazerPedido(self, pedido, dadosPagamento):
        try:
            pedidoFeito = self.__controladorPedido.fazerPedido(pedido, dadosPagamento)
            response = jsonify(pedidoFeito)
        except:
            response = Response(404)
        return response