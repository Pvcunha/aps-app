from dataclasses import dataclass
from model.negocio.estoque.produto import Produto

@dataclass(frozen=True)
class Item:
    produto: Produto
    qtd: int
