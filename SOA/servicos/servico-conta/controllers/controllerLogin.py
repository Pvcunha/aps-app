from model.negocio.usuario import Usuario
from model.negocio.fachada import Fachada
from typing import Dict
from flask import Response, jsonify
import traceback

class ControllerLogin:

    def __init__(self):
        self.fachada = Fachada()
    
    def validaLogin(self, data) -> Response:
        usuario = Usuario(id=-1, email=data['email'], senha=data['senha'], tipo=data['tipo'], cpf=None)
        
        try:
            usuarioLogado = self.fachada.validaLogin(usuario)
            print('usuario logado', usuarioLogado)
            response = jsonify({'id': usuarioLogado.id, 'email': usuarioLogado.email}), 200
        except Exception as err:
            traceback.print_exc()
            response = jsonify({"erro": "Bad Login"}), 409
        
        return response
    
    def validaSessao(self, data) -> Response:
        print(data)
        token = {'email': data['email'], 'id': data['id'], 'tipo': data['tipo']} 

        try:
            sessao = self.fachada.validaSessao(token)
            response = jsonify({'ok': "sessao ok"}), 200
        except Exception as err:
            traceback.print_exc()
            response = jsonify({"erro": "Nao Autorizado"}), 404
        
        return response