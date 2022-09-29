class Movement:

    def __init__(self, date, description, complement):
        self.date = date
        self.description = description
        self.complement = complement

    def json(self):
        return {
            "Data": self.date,
            "Descrição": self.description,
            "Complemento": self.complement
        }

    def set_date(self, date):
        self.date = date

    def set_description(self, description):
        self.description = description

    def set_complement(self, complement):
        self.complement = complement

    def __str__(self):
        print(self.date, self.description, self.complement)
