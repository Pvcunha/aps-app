from flask import Flask, request

from controllers.controllerCadastro import ControllerCadastro

def criaApp():
    app = Flask(__name__)
    cadastroController = ControllerCadastro()

    @app.route('/')
    def home():
        return "hello world"

    @app.post('/cadastro')
    def cadastro():
        data = request.json
        return cadastroController.cadastraUsuario(data)

    return app

if __name__ == '__main__':
    criaApp().run(debug=True, host="0.0.0.0", port=3000)