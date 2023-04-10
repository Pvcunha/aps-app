from model.negocio.estoque.item import Item
from flask import Flask, request

from controllers.controllerEstoque import ControllerEstoque

def criaApp():
    app = Flask(__name__)
    estoqueController = ControllerEstoque()

    @app.route('/')
    def home():
        return "hello world"

    @app.post('/verificaDisponibilidade')
    def verifica():
        data = request.json
        id = data['id']
        qtd = data['qtd']
        return estoqueController.verificaDisponibilidade(id,qtd)

    @app.post('/atualizaMenosItem')
    def menos():
        data = request.json
        id = data['id']
        qtd = data['qtd']
        return estoqueController.atualizaMenos(id,qtd)

    @app.post('/atualizaMaisItem')
    def mais():
        data = request.json
        id = data['id']
        qtd = data['qtd']
        return estoqueController.atualizaMais(id,qtd)

    @app.route('/listaItens')
    def itens():
        data = request.json
        return estoqueController.listaItens()
    
    return app

if __name__ == '__main__':
    criaApp().run(debug=True, host="0.0.0.0", port=3000)