from dataclasses import dataclass
from model.negocio.estoque.produto import Produto

@dataclass
class Item:
    produto: Produto
    qtd: int
