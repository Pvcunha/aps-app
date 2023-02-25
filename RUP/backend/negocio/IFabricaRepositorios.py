from abc import ABC, ABCMeta, abstractmethod

class IFabricaRepositorios(metaclass=ABCMeta):
    
    @abstractmethod
    def criaRepositorioClientesMemoria():
        pass