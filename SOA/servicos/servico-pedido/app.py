from flask import Flask, request
from controllers.controllerPedido import ControllerPedido

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
    criaApp().run(debug=True, host="0.0.0.0", port=3001)