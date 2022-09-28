from court import pattern


class ConfigurationRequisition(pattern.Court):

    def __init__(self, cnj):
        super().__init__()
        self.cnj = cnj
        self.root_url = "https://www2.tjal.jus.br/cposg5/search.do?"
        self.url_request = self.root_url + self.configure_route()

    def configure_route(self):
        dict_route = {
            "conversationId": "",
            "paginaConsulta": "0",
            "cbPesquisa": "NUMPROC",
            "numeroDigitoAnoUnificado": self.cnj[:15],
            "foroNumeroUnificado": self.cnj.split('.')[-1],
            "dePesquisaNuUnificado": self.cnj,
            "dePesquisa": "",
            "tipoNuProcesso": "UNIFICADO"
        }
        list_route = []
        for key, value in dict_route.items():
            list_route.append(key + "=" + value)
        return "&".join(list_route)

    def sub_query(self, selected_process):
        return "https://www2.tjal.jus.br/cposg5/show.do?" + f"processo.codigo={selected_process}"
