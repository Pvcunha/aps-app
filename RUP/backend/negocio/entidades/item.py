from dataclasses import dataclass
from negocio.entidades.produto import Produto

@dataclass(frozen=True)
class Item:
    produto: Produto
    qtd: int
