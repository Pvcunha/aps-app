from negocio.entidades.item import Item
from negocio.registros.registroEstoque import RegistroEstoque
from utils.utils import Injector
from typing import List

class ControladorEstoque:

    def __init__(self) -> None:
        injector = Injector()
        self.registroEstoque = RegistroEstoque(injector.repositorioEstoque)
        
    def verificaDisponibilidade(self, produtoid: int, qtdInteresse: int) -> Item:
        return self.registroEstoque.checaProduto(produtoid, qtdInteresse)

    def pegaEstoque(self) -> List[Item]:
        return self.registroEstoque.pegaEstoque()