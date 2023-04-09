from model.negocio.estoque.item import Item
from model.negocio.estoque.produto import Produto

class Estoque:
    def __init__(self):
        self.itens = [Item(Produto("Coxinha", 3.5, 0), 5), Item(Produto("Empada", 2.0, 1), 3), Item(Produto("Croissant", 5.0, 2), 6)]