from typing import Tuple
from flask import jsonify, Response
from utils.utils import SingletonMeta
from negocio.entidades.cliente import Cliente
from negocio.controladores.controladorLogin import ControladorLogin
from negocio.controladores.controladorCadastro import ControladorCadastro
from interface_negocio_dados.iFabricaRepositorios import IFabricaAbstrataRepositorios
from negocio.fabricaRepositoriosMemoria import FabricaRepositoriosMemoria
from utils.utils import myContainer

class Fachada(metaclass=SingletonMeta):
    
    def __init__(self, db_type: str='padrao'):
        if db_type == 'padrao':
            self.__fabricaRepositorio = FabricaRepositoriosMemoria()
        else:
            pass

        repositorioClientes = self.__fabricaRepositorio.criaRepositorioClientes()
        repositorioEstoque = self.__fabricaRepositorio.criaRepositorioEstoque()
        repositorioPedidos = self.__fabricaRepositorio.criaRepositorioPedido()
        self.repo = repositorioClientes
        myContainer.repositorioClientes.override(repositorioClientes)
        myContainer.repositorioEstoque.override(repositorioEstoque)
        myContainer.repositorioPedidos.override(repositorioPedidos)
        
        self.__controladorLogin = ControladorLogin()
        self.__controladorCadastro = ControladorCadastro()
        
    def pegaalgo(self):
        return jsonify(self.repo.getAll())
    
    def fazLogin(self, email: str, senha: str) -> Response:
        try:
            cliente = self.__controladorLogin.loginCliente(email, senha)
            response = jsonify(cliente.__dict__)
            response.status_code = 200
            return response
        except:
            return Response(status=204)

    def fazCadastro(self, email: str, senha: str, cpf: str) -> Response:
        try:
            cliente = self.__controladorCadastro.cadastroCliente(email, senha, cpf)
            response = jsonify(cliente.__dict__)
            response.status_code = 200
            return response
        except:
            return Response(status=400)
            