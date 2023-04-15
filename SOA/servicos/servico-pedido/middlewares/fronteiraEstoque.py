from utils.comunicacao import comunicar
from typing import List, Union, Dict
import traceback

class FronteiraEstoque:

    @classmethod
    def alterarEstoque(cls, produtos: List[Dict[str, Union[str, int]]], rota: str):
        data = {"produtos": produtos }
        try:
            response = comunicar(f'http://servico-fachada:3333/estoque/{rota}', data=data,
                                 method='POST', headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return True
        except Exception as err:
            traceback.print_exc()
        
        return False
    
    @classmethod
    def verificaDisponibilidade(cls, produto: List[Dict[str, Union[str, int]]]):
        data = {"id": produto['id'], 'qtd': produto['qtd']}
        try:
            response = comunicar('http://servico-fachada:3333/estoque/verificaDisponibilidade', data=data,
                                 method='POST', headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return True
        except Exception as err:
            traceback.print_exc()
        
        return False