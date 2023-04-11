from model.negocio.fachada import Fachada
from model.negocio.usuario.usuario import Usuario
from flask import jsonify, Response
import traceback

class ControllerCadastro:

    def __init__(self):
        self.fachada: Fachada = Fachada()
    
    def cadastraUsuario(self, data) -> Response:
        email, senha, cpf, tipo = data['email'], data['senha'], data['cpf'], data['tipo']
        novoUsuario = Usuario(id=-1, email=email, senha=senha, cpf=cpf, tipo=tipo)
        try:
            usuario = self.fachada.cadastraUsuario(novoUsuario)
            response = jsonify({'id': usuario.id, 'email': usuario.email})
        except Exception as err:
            traceback.print_exc()
            response = Response(409)

        return response