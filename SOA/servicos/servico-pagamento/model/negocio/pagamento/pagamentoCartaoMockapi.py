import requests
import json
from typing import Dict, Any
from ..pedido.pedido import Pedido
from middlewares.fronteiraMockAPI import PagamentoCartaoMockapi

class PagamentoCartaoMockapi:
    def pagar(self, **args) -> Dict[Pedido, Any]:
        return PagamentoCartaoMockapi.pagar(args)
