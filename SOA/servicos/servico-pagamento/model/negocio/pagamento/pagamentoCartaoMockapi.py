import requests
import json
from typing import Dict, Any
from ..pedido.pedido import Pedido

class PagamentoCartaoMockapi:
    def pagar(self, **args) -> Dict[Pedido, Any]:
        return self.pagar(args)
