from dataclasses import dataclass
from typing import List, Dict, Union

@dataclass
class Pedido:
    id: str
    precoTotal: float