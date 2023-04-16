from typing import Dict
from model.negocio.fabricaPagamento import FabricaPagamento
from model.negocio.pagamento.pedido import Pedido
from model.negocio.pagamento.pagamento import Pagamento
from model.negocio.adapters.adapterPagamentoCartao import AdapterPagamentoCartaoMockapi

class FabricaPagamentoCartao(FabricaPagamento):
    
    def criaPagamento(self, pedido: Pedido, dadosPagamento: Dict) -> Pagamento:
        print("AQUI***************************")
        print(pedido)
        print(dadosPagamento)
        if dadosPagamento['bandeira'] == 'mockapi':
            adapterPagamentoCartao = AdapterPagamentoCartaoMockapi(pedido, numeroCartao=dadosPagamento['numeroCartao'], 
                                                               cpfTitular=dadosPagamento['cpf'], nomeTitular=dadosPagamento['nomeTitular'], 
                                                               cvv=dadosPagamento['cvv'], vencimento=dadosPagamento['vencimento'])
        else:
            raise Exception("Bandeira Nao implementada")

        pagamento = adapterPagamentoCartao.pagar()
        return pagamento