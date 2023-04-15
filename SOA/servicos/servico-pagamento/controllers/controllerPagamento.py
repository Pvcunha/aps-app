from model.negocio.fachada import Fachada
from flask import jsonify, Response
import traceback

class ControllerPagamento:

    def __init__(self):
        self.fachada: Fachada = Fachada()
    
    def fazPagamento(self, data) -> Response:
        pedido = data['pedido']
        dadosPagamento = data['dadosDoPagamento']
        try:
            pagamentoFeito = self.fachada.fazPagamentopagamento(pedido,dadosPagamento)
            response = jsonify(pagamentoFeito)
        except:
            response = Response(404)
        return response