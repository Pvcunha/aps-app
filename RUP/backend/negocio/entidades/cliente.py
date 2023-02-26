from dataclasses import dataclass

@dataclass(frozen=True)
class Cliente:
    email: str
    cpf: str
    senha: str
    id: int