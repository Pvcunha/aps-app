import requests
import json
from typing import Dict
from typing import Any
from negocio.entidades.pedido import Pedido

class PagamentoCartaoMockapi:

    apiurl = 'https://63fb5d347a045e192b67d6d9.mockapi.io/api/v1/pagamentoCartao'

    def pagar(self, **args) -> Dict[Pedido, Any]:
        print("DEU BOMM ?dsdsddsdssds?")
        mockapi_data = {'Pedido': args['pedido'].__dict__, 
                        'Dados Pagamento': {'Numero Cartao': args['numeroCartao'], 
                                            'CVV': args['cvv'],
                                            'Data Vencimento': args['vencimento']}}
        response = requests.post(url=self.apiurl, data=mockapi_data)
        data = json.loads(response.content.decode('utf-8'))
        print("DEU BOMM ??")
        return data
