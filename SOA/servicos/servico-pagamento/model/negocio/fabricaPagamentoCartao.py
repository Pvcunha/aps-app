from typing import Dict
from model.negocio.fabricaPagamento import FabricaPagamento
from model.negocio.pedido.pedido import Pedido
from model.negocio.pagamento.pagamento import Pagamento
from model.negocio.adapters.adapterPagamentoCartao import AdapterPagamentoCartaoMockapi
from middlewares.fronteiraPedido import FronteiraPedido
import traceback

class FabricaPagamentoCartao(FabricaPagamento):
    
    def criaPagamento(self, pedido: Pedido, dadosPagamento: Dict) -> Pagamento:
        if dadosPagamento['bandeira'] == 'mockapi':
            
            adapterPagamentoCartao = AdapterPagamentoCartaoMockapi(pedido, numeroCartao=dadosPagamento['numeroCartao'], 
                                                               cpfTitular=dadosPagamento['cpf'], nomeTitular=dadosPagamento['nomeTitular'], 
                                                               cvv=dadosPagamento['cvv'], vencimento=dadosPagamento['vencimento'])
        
        else:
            raise Exception("Bandeira Nao implementada")

        pagamento = adapterPagamentoCartao.pagar()
        if pagamento['concluido'] == False:
            FronteiraPedido.cancelaPedido(pedido.id)
        else:
            FronteiraPedido.confirmaPedido(pedido.id)
        return pagamento