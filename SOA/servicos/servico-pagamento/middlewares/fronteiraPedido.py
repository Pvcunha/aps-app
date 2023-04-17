from utils.comunicacao import comunicar
import traceback

class FronteiraPedido:

    @classmethod
    def cancelaPedido(cls, pedidoID: str):
        data = {"pedidoID": pedidoID}
        try:
            response = comunicar('http://servico-fachada:3333/pedido/cancelaPedido', data=data,
                                 method='POST', headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return True
        except Exception as err:
            traceback.print_exc()
        
        return False
    
    @classmethod
    def confirmaPedido(cls, pedidoID: str):
        data = {"pedidoID": pedidoID}
        try:
            response = comunicar('http://servico-fachada:3333/pedido/confirmaPedido', data=data,
                                 method='POST', headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return True
        except Exception as err:
            traceback.print_exc()
        
        return False