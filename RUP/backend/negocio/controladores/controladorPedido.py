from negocio.entidades.item import Item


class ControladorPedido:

    def __init__(self,registroProduto) -> None:
        self.registroProduto = registroProduto

    def pegaItemEstoque(self,nome) -> Item:
        self.registroProduto.itemEstoque(nome)   