from flask import Flask, jsonify
from negocio import Fachada

app = Flask(__name__)

fachada = Fachada()

@app.route('/')
def hello_world():
    return fachada.pegaalgo()

@app.route('/login/<email>/<senha>')
def login(email, senha):
    res = fachada.fazLogin(email, senha)
    return res

@app.route('/produtos/<int:produtoid>/<int:qtd>')
def verificaDisponibilidade(produtoid, qtd):
    return fachada.verificaDisponibilidade(produtoid, qtd)

@app.route('/produtos')
def listaProdutos():
    return fachada.listaItens()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)