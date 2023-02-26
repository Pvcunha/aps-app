from typing import Dict
from negocio.fabricas.fabricaPagamento import FabricaPagamento
from negocio.entidades.pedido import Pedido
from negocio.entidades.pagamento import Pagamento
from negocio.adapters.adapterPagamentoCartao import AdapterPagamentoCartaoMockapi

class FabricaPagamentoCartao(FabricaPagamento):
    
    def criaPagamento(self, pedido: Pedido, dadosPagamento: Dict) -> Pagamento:
        if dadosPagamento['bandeira'] == 'mockapi':
            adapterPagamentoCartao = AdapterPagamentoCartaoMockapi(pedido, numeroCartao=dadosPagamento['numeroCartao'], 
                                                               cpfTitular=dadosPagamento['cpf'], nomeTitular=dadosPagamento['nomeTitular'], 
                                                               cvv=dadosPagamento['cvv'], vencimento=dadosPagamento['vencimento'])
        else:
            raise Exception("Bandeira Nao implementada")

        pagamento = adapterPagamentoCartao.pagar()
        return pagamento