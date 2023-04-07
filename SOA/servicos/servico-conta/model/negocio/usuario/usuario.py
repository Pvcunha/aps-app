from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    email: str
    senha: str
    cpf: str
    tipo: str
