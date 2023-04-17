from model.negocio.fachada import Fachada
from flask import jsonify, Response
from model.negocio.pedido.pedido import Pedido
import traceback

class ControllerPagamento:

    def __init__(self):
        self.fachada: Fachada = Fachada()
    
    def fazPagamento(self, data) -> Response:
        pedido = Pedido(id=data["pedido"]["id"], precoTotal=data['pedido']['precoTotal'])
        dadosPagamento = data['dadosDoPagamento']
        try:
            pagamentoFeito = self.fachada.fazPagamento(pedido, dadosPagamento)
            if pagamentoFeito['concluido'] == True:
                response = jsonify({'message': 'Pagamento Concluido'}), 202
            else:
                response = jsonify({'message': 'Erro ao concluir o pagamento'}), 402
        except:
            traceback.print_exc()
            response = jsonify({'message': 'Erro de codigo'}), 406
            
        return response