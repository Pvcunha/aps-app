from dataclasses import dataclass
from negocio.Estoque.produto import Produto

@dataclass(frozen=True)
class Item:
    produto: Produto
    qtd: int
