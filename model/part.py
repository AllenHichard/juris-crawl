class Part:

    def __init__(self, pole, clients, lawyers):
        self.pole = pole
        self.clients = clients
        self.lawyers = lawyers

    def json(self):
        return {
            self.pole: {
                "Envolvidos": [client for client in self.clients] + [attorney for attorney in self.lawyers],
            }
        }

    def set_lawyers(self, lawyers):
        self.lawyers = lawyers

    def set_clients(self, clients):
        self.clients = clients
