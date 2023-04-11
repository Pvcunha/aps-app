from utils.comunicacao import comunicar
import json
import traceback
class MiddlewareAuth:

    @classmethod
    def autentica(cls, data) -> bool:
        print(data)
        dadoAutentica = {'id': data['usuarioID'], 'email': data['usuarioEmail'], 'tipo': data['usuarioTipo']}
        try:
            response = comunicar('http://localhost:3000/validaSessao', 
                                 data=dadoAutentica, method='POST', 
                                 headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return True
        except:
            return False