from dependency_injector  import containers, providers
import enum
import json

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Injector(metaclass=SingletonMeta):

    repositorioClientes = None

    repositorioEstoque = None
    
    repositorioPedidos = None

class StatusPedido(enum.Enum):
    FALHA=0
    CONCLUIDO=1
    ESPERANDO=2

    def get(self, num):
        if num == 0:
            return self.FALHA
        elif num == 1:
            return self.ESPERANDO
        else:
            return self.CONCLUIDO
        
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, StatusPedido):
            return obj.value
        return super().default(obj)