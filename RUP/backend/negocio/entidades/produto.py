from dataclasses import dataclass

@dataclass
class Produto:
    def __init__(self,nome,valor,id):
        self.nome=nome
        self.valor=valor
        self.id=id