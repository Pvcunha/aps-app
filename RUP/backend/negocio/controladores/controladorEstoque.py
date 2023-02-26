from negocio.entidades.item import Item
from negocio.registros.registroEstoque import RegistroEstoque

class ControladorEstoque:

    def __init__(self) -> Item:
        self.registroEstoque = RegistroEstoque()
        pass
    
