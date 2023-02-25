from dataclasses import dataclass
from produto import Produto
@dataclass
class Item:
    def __init__(self,produto,qtd):
        self.produto=produto
        self.qtd=qtd
