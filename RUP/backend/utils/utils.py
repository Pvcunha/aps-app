from dependency_injector  import containers, providers
import enum

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
    ESPERANDO=1
    CONCLUIDO=2
