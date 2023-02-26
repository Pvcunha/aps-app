from interface_negocio_dados.iFabricaRepositorios import IFabricaAbstrataRepositorios
from dependency_injector  import containers, providers
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MyContainer(containers.DeclarativeContainer):

    repositorioClientes = providers.Object(None)

    repositorioEstoque = providers.Object(None)
    
    repositorioPedidos = providers.Object(None)

myContainer = MyContainer()