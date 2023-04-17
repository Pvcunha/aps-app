from flask import Flask, request
from controllers.controllerPedido import ControllerPedido
from middlewares.auth import MiddlewareAuth
import consul

def criaApp():
    app = Flask(__name__)
    
    controllerPedido = ControllerPedido()


    @app.route('/')
    def home():
        return "hello world"
    
    @app.route('/criaPedido', methods=['POST'])
    def criaPedido():
        data = request.json
        return controllerPedido.criaPedido(data)

    @app.route('/buscaPedido', methods=['POST'])
    def buscaPedido():
        data = request.json
        return controllerPedido.buscaPedido(data)
    
    @app.route('/cancelaPedido', methods=['DELETE'])
    def cancelaPedido():
        data = request.json
        return controllerPedido.cancelaPedido(data)

    @app.route('/confirmaPedido', methods=['PUT'])
    def confirmaPedido():
        data = request.json
        return controllerPedido.confirmaPedido(data)

    @app.route('/saude')
    def saude():
        return "Confirmacao de saude"
    
    return app

if __name__ == '__main__':
    client = consul.Consul(host='discovery', port=8500)
    
    servico_nome = 'servico-pedido'
    servico_porta = 3001

    client.agent.service.register(
        name=servico_nome,
        service_id=servico_nome,
        address=servico_nome,
        port=servico_porta,
        check=consul.Check.http(f'http://servico-pedido:{servico_porta}/saude', interval='10s')    
    )

    criaApp().run(debug=True, host="0.0.0.0", port=3001)