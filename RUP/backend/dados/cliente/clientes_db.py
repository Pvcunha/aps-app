from negocio.entidades.cliente import Cliente

class ClientesContainer:

    def __init__(self):
        self.clientes = [Cliente(email='a', senha='b', id=0)]
        self.id_count = 1
    
    def printClientes(self):
        print(self.clientes)

clientes = ClientesContainer()