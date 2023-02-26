import requests
import json

class PagamentoCartaoMockapi:

    apiurl = 'https://63fb5d347a045e192b67d6d9.mockapi.io/api/v1/pagamentoCartao'

    def pagar(self, **args):
        dadosPagamento = args['dadosPagamento']
        mockapi_data = {'Pedido': args['pedido'].__dict__, 
                        'Dados Pagamento': {'Numero Cartao': dadosPagamento['numeroCartao'], 
                                            'CVV': dadosPagamento['cvv'],
                                            'Data Vencimento': dadosPagamento['dataVencimento']}}
        response = requests.post(url=self.apiurl, data=mockapi_data)
        data = json.loads(response.content.decode('utf-8'))
        return data
