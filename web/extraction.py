from model import process
import bs4 as bs


class Extraction:

    def __init__(self, html):
        self.html = html
        self.soap = bs.BeautifulSoup(html, "html.parser")
        self.process = process.Process()
        self.lookup_dictionary = self.configure_query_dictionary()

    def configure_query_dictionary(self):
        return {
            "justice_class": ("classeProcesso", self.process.set_justice_class),
            "area": ("areaProcesso", self.process.set_area),
            "subject": ("assuntoProcesso", self.process.set_subject),
            "distribution_date": ("dataHoraDistribuicaoProcesso", self.process.set_distribution_date),
            "judge": ("juizProcesso", self.process.set_judge),
            "action_value": ("valorAcaoProcesso", self.process.set_action_value),
            "parts": ("tablePartesPrincipais", self.process.add_parts),
            "movements": ("tabelaUltimasMovimentacoes", self.process.add_movements)
        }

    def format_response(self, data_field):
        validate_data_field = filter(lambda caracter: caracter not in ["\t", "\r", "\n"], data_field.strip())
        return "".join(list(validate_data_field)).strip()

    def __load_header(self, data_field, set_value_function):
        if data_field:
            data_field = self.format_response(data_field.text)
            set_value_function(data_field)
        else:
            set_value_function("Indisponível")

    def load(self):
        for key, value in self.lookup_dictionary.items():
            id_html, set_value_function = value
            data_field = self.soap.find(id=id_html)
            if "parts" in key:
                self.__load_parts(data_field, set_value_function)
            elif "movements" in key:
                self.__load_movements(data_field, set_value_function)
                pass
            else:
                self.__load_header(data_field, set_value_function)

    def __load_movements(self, data_field, set_value_function):
        movement_lines = data_field.findAll("tr")
        for movement_line in movement_lines:
            date, description = "", ""
            movement_columns = movement_line.findAll("td")
            for movement_column in movement_columns:
                if "class" in movement_column.attrs:
                    if "data" in movement_column["class"][0]:
                        date = movement_column.text
                        date = self.format_response(date)
                    elif "descricao" in movement_column["class"][0]:
                        link = movement_column.find("a")
                        description = self.format_response(link.text) if link else ""
                        description_next = movement_column.next
                        description += self.format_response(description_next)
            span = movement_line.find("span").next
            complement = self.format_response(span)
            set_value_function(date, description, complement)

    def __load_parts(self, data_field, set_value_function):
        part_lines = data_field.findAll("tr")
        for part in part_lines:
            pole = part.find("td", {"class", "label"})
            pole = self.format_response(pole.text)
            involved = part.find("td", {"class": "nomeParteEAdvogado"})
            clients, lawyers = self.__capture_involved_parties(involved)
            set_value_function(pole, clients, lawyers)

    def __capture_involved_parties(self, involved):
        clients, lawyers = [], []
        involved_iter = iter(involved)
        client = next(involved_iter)
        client = self.format_response(client)
        clients.append(client)
        for elem in involved_iter:
            if "span" in str(elem):
                attorney = next(involved_iter)
                attorney = self.format_response(attorney)
                lawyers.append(attorney)
        return clients, lawyers
