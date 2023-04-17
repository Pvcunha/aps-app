from flask import Flask, request
from controllers.controllerPagamento import ControllerPagamento
from flask_cors import CORS
import consul 

def criaApp():
    app = Flask(__name__)
    CORS(app)
    pagamentoController = ControllerPagamento()

    client = consul.Consul(host='discovery', port=8500)
    
    servico_nome = 'servico-pagamento'
    servico_porta = 3003

    client.agent.service.register(
        name=servico_nome,
        service_id=servico_nome,
        address=servico_nome,
        port=servico_porta,
        check=consul.Check.http(f'http://servico-pagamento:{servico_porta}/saude', interval='10s')    
    )

    @app.route('/')
    def home():
        return "hello world"

    @app.post('/pagamento')
    def pagamento():
        data = request.json
        return pagamentoController.fazPagamento(data)

    @app.route('/saude')
    def saude():
        return "vivo"
    
    return app


if __name__ == '__main__':
    criaApp().run(debug=True, host="0.0.0.0", port=3003)