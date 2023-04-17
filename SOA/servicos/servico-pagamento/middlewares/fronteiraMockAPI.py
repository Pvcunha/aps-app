import json
import requests

class PagamentoCartaoMockapi:

    @classmethod
    def pagar(cls, **args):
        apiurl = 'https://63fb5d347a045e192b67d6d9.mockapi.io/api/v1/pagamentoCartao'
        mockapi_data = {
                       'Dados Pagamento': {'Numero Cartao': args['numeroCartao'], 
                                            'CVV': args['cvv'],
                                            'Data Vencimento': args['vencimento']}}
        response = requests.post(url=apiurl, data=mockapi_data)
        data = json.loads(response.content.decode('utf-8'))
        return data
