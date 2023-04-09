from model.negocio.fachada import Fachada
from model.negocio.estoque.item import Item
from model.negocio.estoque.produto import Produto
from flask import jsonify, Response
import traceback
from utils.exceptions import EstoqueInsuficienteException

class ControllerEstoque:

    def __init__(self):
        self.fachada: Fachada = Fachada()
    

    def verificaDisponibilidade(self, produtoId: int, qtdInteresse: int):
        # mudar na arquitetura de adicionarAoCarrinho para verificarDisponibilidade
        try:
            novoProduto = Produto(id = produtoId)
            novoItem = Item(produto=novoProduto,qtd= qtdInteresse)
            item = self.fachada.verificaDisponibilidade(novoItem)
            response = jsonify(item.__dict__)
            response.status_code = 200
            return response
        except EstoqueInsuficienteException as err:
            return Response(err.message, status=400)

       
    def listaItens(self):
        itens = self.fachada.listaItens()
        itens_dicts = [item.__dict__ for item in itens]
        return jsonify(itens_dicts)