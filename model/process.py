from model import movement, part


class Process:

    def __init__(self):
        self.justice_class = None
        self.area = None
        self.subject = None
        self.distribution_date = None
        self.judge = None
        self.action_value = None
        self.parts = []
        self.movements = []

    def json(self):
        return {
            "Classe": self.justice_class,
            "Área": self.area,
            "Assunto": self.subject,
            "Data de Distribuição": self.distribution_date,
            "Juiz": self.judge,
            "Valor da Ação": self.action_value,
            "Partes do Processo": [part_value.json() for part_value in self.parts],
            "Lista das ùltimas Movimentações": [movement_value.json() for movement_value in self.movements]
        }

    def __str__(self):
        print(self.justice_class)
        print(self.area)
        print(self.subject)
        print(self.distribution_date)
        print(self.judge)
        print(self.action_value)
        for p in self.parts:
            p.__str__()
        for m in self.movements:
            m.__str__()

    def set_justice_class(self, justice_class):
        self.justice_class = justice_class

    def set_area(self, area):
        self.area = area

    def set_subject(self, subject):
        self.subject = subject

    def set_distribution_date(self, distribution_date):
        self.distribution_date = distribution_date

    def set_judge(self, judge):
        self.judge = judge

    def set_action_value(self, action_value):
        self.action_value = action_value.replace(" ", "").replace("R$", "")

    def add_parts(self, pole, clients, lawyers):
        self.parts.append(part.Part(pole, clients, lawyers))

    def add_movements(self, date, description, complement):
        self.movements.append(movement.Movement(date, description, complement))
