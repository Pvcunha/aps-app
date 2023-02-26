from dataclasses import dataclass
from negocio.entidades.produto import Produto

@dataclass
class Item:
    def __init__(self, produto: Produto, qtd: int):
        self.produto=produto
        self.qtd=qtd
