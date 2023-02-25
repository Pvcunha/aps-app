from dataclasses import dataclass

@dataclass
class Cliente:
    def __init__(self, email, senha, id=-1):
        self.email = email
        self.senha = senha
        self.id = id