from flask import Flask, request
from controllers.controllerPagamento import ControllerPagamento
from flask_cors import CORS

def criaApp():
    app = Flask(__name__)
    CORS(app)
    pagamentoController = ControllerPagamento()

    @app.route('/')
    def home():
        return "hello world"

    @app.post('/pagamento')
    def pagamento():
        data = request.json
        return pagamentoController.fazPagamento(data)

    return app


if __name__ == '__main__':
    criaApp().run(debug=True, host="0.0.0.0", port=3000)