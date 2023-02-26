from negocio.entidades.item import Item
from interface_negocio_dados.iRepositorioEstoque import IRepositorioEstoque
from negocio.entidades.pedido import Pedido
from utils.exceptions import EstoqueInsuficienteException
from typing import List

class RegistroEstoque:

    def __init__(self, repositorioItem: IRepositorioEstoque):
        self.repositorioItemMemoria = repositorioItem
        pass

    def checaProduto(self, produtoid: int, qtdInteresse: int) -> Item:
        item = self.repositorioItemMemoria.buscarItem(produtoid)
        
        if qtdInteresse > item.qtd:
            raise EstoqueInsuficienteException(f"Nao temos quantidade suficiente de {item.produto.nome}")
        
        return item

    def atualizarEstoque(self, pedido: Pedido):
        for item in pedido.itens:
            self.repositorioItemMemoria.atualizarItem(item.produto.id, item.qtd)

    def pegaEstoque(self) -> List[Item]:
        return self.repositorioItemMemoria.getAll()