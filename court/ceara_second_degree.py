from court import pattern

class ConfigurationRequisition(pattern.Court):
    def __init__(self, cnj):
        super().__init__()
        self.cnj = cnj
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
        return "https://www2.tjal.jus.br/cposg5/show.do?" + f"processo.codigo={selected_process}"


# class Tjal:
#
#     def __init__(self, session, numero_processo):
#         self.session = session
#         self.url = "" \
#               "conversationId=&" \
#               "paginaConsulta=0&" \
#               "cbPesquisa=NUMPROC&" \
#               f"numeroDigitoAnoUnificado={numero_processo[:15]}&" \
#               f"foroNumeroUnificado={numero_processo.split('.')[-1]}&" \
#               f"dePesquisaNuUnificado={numero_processo}&" \
#               "dePesquisaNuUnificado=UNIFICADO&" \
#               "dePesquisa=&" \
#               "tipoNuProcesso=UNIFICADO"
