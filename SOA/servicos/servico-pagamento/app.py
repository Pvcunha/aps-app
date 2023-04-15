from flask import Flask, request
#import consul
from controllers.controllerPagamento import ControllerPagamento

def criaApp():
    app = Flask(__name__)
    pagamentoController = ControllerPagamento()

    @app.route('/')
    def home():
        return "hello world"

    @app.post('/pagamento')
    def pagamento():
        data = request.json
        return pagamentoController.fazPagamento(data)

    return app

#if __name__ == '__main__':
#    client = consul.Consul(host='discovery', port=8500)
#    
#    service_name = 'servico-conta'
#    service_port = 3000
#
#    client.agent.service.register(
#        
#        name=service_name,
#        service_id=service_name,
#        port=service_port,
#        check=consul.Check.http(f'http://servico-conta:{service_port}', interval='10s')    
#    )
#
#    criaApp().run(debug=True, host="0.0.0.0", port=3000)