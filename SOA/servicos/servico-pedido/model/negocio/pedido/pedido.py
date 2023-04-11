from dataclasses import dataclass
from typing import List, Dict, Union

@dataclass
class Pedido:
    id: str
    clienteID: str
    produtos: List[Dict[str, Union[str, float]]]
    precoTotal: float
    status: str