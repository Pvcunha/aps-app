from typing import List
from dataclasses import dataclass
from negocio.entidades.item import Item
from utils.utils import StatusPedido

@dataclass(frozen=True)
class Pedido:
    id: int
    clienteId: int
    valor: float
    itens: List[Item]
    status: StatusPedido
