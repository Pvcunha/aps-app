from model.negocio.fachada import Fachada
from model.negocio.pedido.pedido import Pedido
from flask import jsonify, Response
import traceback

class ControllerPedido:

    def __init__(self):
        self.fachada: Fachada = Fachada()
    
    def criaPedido(self, data) -> Response:
        #TODO inserir auth

        pedido = Pedido(id="xxx", clienteID=data['clienteID'], precoTotal=0.0, produtos=data['produtos'], status='esperando pagamento')
        print(pedido.produtos)
        try:
            pedido = self.fachada.criaPedido(pedido)
            response = jsonify({'pedidoID': pedido.id, 'precoTotal': pedido.precoTotal}), 201
        except Exception as err:
            traceback.print_exc()
            response = jsonify({'erro': 'Nao foi possivel criar o pedido'}), 409
        
        return response
    
    def cancelaPedido(self, data) -> Response:
        pedidoID = data['pedidoID']
        try:
            pedidoCancelado = self.fachada.cancelaPedido(pedidoID)
            response = jsonify({"message": "Pedido Cancelado", "pedidoID": pedidoID}), 201
        except Exception as err:
            traceback.print_exc()
            response = jsonify({"message": "erro ao cancelar pedido", "pedidoID": pedidoID}), 409

        return response 
    
    def confirmaPedido(self, data) -> Response:
        pedidoID = data['pedidoID']
        try:
            pedidoConfirmado = self.fachada.confirmaPedido(pedidoID)
            response = jsonify({"message": "Pedido Confirmado", "pedidoID": pedidoConfirmado.id}), 201
        except:
            traceback.print_exc()
            response = jsonify({"message": "erro ao confirmar pedido"}), 409

        return response
    
    def buscaPedido(self, data) -> Response:
        return jsonify({"message": "Not implemented"}), 501
    