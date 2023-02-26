from negocio.entidades.item import Item
from negocio.entidades.produto import Produto

class Estoque:
    def __init__(self):
        self.itens = [Item(Produto("Coxinha", 3.5, 0), 5), Item(Produto("Empada", 2.0, 1), 3), Item(Produto("Croissant", 5.0, 2), 6)]