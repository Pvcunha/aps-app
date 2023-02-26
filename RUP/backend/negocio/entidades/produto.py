from dataclasses import dataclass

@dataclass(frozen=True)
class Produto:
    nome: str
    valor: float
    id: int