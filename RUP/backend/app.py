from flask import Flask
from negocio import Fachada

app = Flask(__name__)
fachada = Fachada()
class teste:
    def __init__(self):
        self.a = 10
    
@app.route('/')
def hello_world():
    return fachada.pegaalgo()

@app.route('/login/<email>/<senha>')
def login(email, senha):
    res = fachada.fazLogin(email, senha)
    return res

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)