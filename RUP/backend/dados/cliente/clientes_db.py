from negocio.entidades.cliente import Cliente

class ClientesContainer:

    def __init__(self):
        self.clientes = [Cliente(email='pvc@email.com', senha='123', cpf='12345678900', id=0)]
        self.id_count = 1
    
    def printClientes(self):
        print(self.clientes)

clientesDB = ClientesContainer()
