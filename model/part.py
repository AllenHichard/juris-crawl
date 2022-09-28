class Part:

    def __init__(self, pole, clients, lawyers):
        self.pole = pole
        self.clients = clients
        self.lawyers = lawyers

    def set_lawyers(self,lawyers):
        self.lawyers = lawyers

    def set_clients(self, clients):
        self.clients = clients

    def __str__(self):
        print(self.pole, self.clients, self.lawyers)