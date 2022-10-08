from court import pattern


class ConfigurationRequisition(pattern.Court):

    def __init__(self, cnj):
        super().__init__()
        self.cnj = cnj
        self.state = "Ceará"
        self.degree = "Segundo Grau"
        self.root_url = "https://esaj.tjce.jus.br/cposg5/search.do?"
        self.url_request = self.root_url + self.configure_route()

    def configure_route(self):
        dict_route = {
            "cbPesquisa": "NUMPROC",
            "dePesquisaNuUnificado": self.cnj,
            "tipoNuProcesso": "UNIFICADO"
        }
        list_route = []
        for key, value in dict_route.items():
            list_route.append(key + "=" + value)
        return "&".join(list_route)

    def sub_query(self, selected_process):
        return "https://esaj.tjce.jus.br/cposg5/show.do?" + f"processo.codigo={selected_process}"
