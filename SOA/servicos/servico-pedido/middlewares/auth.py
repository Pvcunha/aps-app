from utils.comunicacao import comunicar
import json
import traceback
class MiddlewareAuth:

    @classmethod
    def autentica(cls, data) -> bool:
        dadoAutentica = {'id': data['usuarioID'], 'email': data['usuarioEmail'], 'tipo': data['usuarioTipo']}
        try:
            response = comunicar('http://servico-fachada:3333/conta/validaSessao', 
                                 data=dadoAutentica, method='POST', 
                                 headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return True
        except:
            return False