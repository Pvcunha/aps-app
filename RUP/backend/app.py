from flask import Flask, jsonify, request
from negocio import Fachada
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

fachada = Fachada()

@app.route('/')
def hello_world():
    return fachada.pegaalgo()

@app.post('/login')
def login():
    data = request.json
    email = data['email']
    senha = data['senha']
    res = fachada.fazLogin(email, senha)
    return res

@app.post('/cadastro')
def cadastro():
    data = request.json
    email = data['email']
    senha = data['senha']
    cpf = data['cpf']
    return fachada.fazCadastro(email, senha, cpf)

@app.post('/finalizarPedido')
def finalizarPedido():
    pedido = request.json['pedido']
    dadosDePagamento = request.json['dadosDoPagamento']
    return fachada.fazerPedido(pedido, dadosDePagamento)


@app.route('/produtos/disponibilidade')
def verificaDisponibilidade(produtoid, qtd):
    return fachada.verificaDisponibilidade(produtoid, qtd)

@app.get('/produtos')
def listaProdutos():
    return fachada.listaItens()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)