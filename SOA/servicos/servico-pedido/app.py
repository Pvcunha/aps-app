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

    return app

if __name__ == '__main__':
    client = consul.Consul(host='discovery', port=8500)
    
    service_name = 'servico-pedido'
    service_port = 3001

    client.agent.service.register(
        
        name=service_name,
        service_id=service_name,
        port=service_port,
        check=consul.Check.http(f'http://servico-pedido:{service_port}', interval='10s')    
    )

    criaApp().run(debug=True, host="0.0.0.0", port=3001)