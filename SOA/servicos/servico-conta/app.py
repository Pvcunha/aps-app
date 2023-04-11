from flask import Flask, request

from controllers.controllerCadastro import ControllerCadastro
from controllers.controllerLogin import ControllerLogin

def criaApp():
    app = Flask(__name__)
    cadastroController = ControllerCadastro()
    loginController = ControllerLogin()

    @app.route('/')
    def home():
        return "hello world"

    @app.post('/cadastro')
    def cadastro():
        data = request.json
        return cadastroController.cadastraUsuario(data)

    @app.route('/login', methods=["POST"])
    def login():
        data = request.json
        return loginController.validaLogin(data)
    
    @app.route('/validaSessao', methods=['POST'])
    def me():
        data = request.json
        return loginController.validaSessao(data)
    
    return app

if __name__ == '__main__':
    import consul
    client = consul.Consul(host='discovery', port=8500)
    
    service_name = 'servico-conta'
    service_port = 3000

    client.agent.service.register(
        
        name=service_name,
        service_id=service_name,
        port=service_port,
        check=consul.Check.http(f'http://servico-conta:{service_port}', interval='10s')    
    )

    criaApp().run(debug=True, host="0.0.0.0", port=3000)