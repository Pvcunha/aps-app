from model.negocio.estoque.item import Item
from flask import Flask, request
from controllers.controllerEstoque import ControllerEstoque

import consul

def criaApp():
    app = Flask(__name__)
    estoqueController = ControllerEstoque()

    client = consul.Consul(host='discovery', port=8500)
    
    servico_nome = 'servico-estoque'
    servico_porta = 3002

    client.agent.service.register(
        name=servico_nome,
        service_id=servico_nome,
        address=servico_nome,
        port=servico_porta,
        check=consul.Check.http(f'http://servico-estoque:{servico_porta}/saude', interval='10s')    
    )

    @app.route('/')
    def home():
        return "hello world"

    @app.post('/verificaDisponibilidade')
    def verifica():
        data = request.json
        id = data['id']
        qtd = data['qtd']
        return estoqueController.verificaDisponibilidade(id,qtd)

    @app.post('/atualizaMenosPedido')
    def menos():
        print(request.json)
        data = request.json['produtos']
        return estoqueController.atualizaMenos(data)

    @app.post('/atualizaMaisPedido')
    def mais():
        data = request.json['produtos']
        itens = data['pedido']
        return estoqueController.atualizaMais(data)

    @app.route('/listaItens')
    def itens():
        data = request.json
        return estoqueController.listaItens()
    
    @app.route('/saude')
    def healthCheck():
        return "ola"
    
    return app

if __name__ == '__main__':

    criaApp().run(debug=True, host="0.0.0.0", port=3002)