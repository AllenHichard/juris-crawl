from court import dict_courts
from web import extraction as soup_web
import bs4 as bs
import urllib3
from urllib3.util.ssl_ import create_urllib3_context


class Session:

    def __init__(self, cnj):
        self.court = None
        self.request = urllib3.PoolManager(ssl_context=self.config_ssl_op_legacy_server_connect())
        self.cnj = cnj.replace(".", "").replace("-", "")
        self.type_court = self.cnj[14:16]
        self.degrees_court = dict_courts[self.type_court]
        self.returned_processes = []
        self.results = dict()

    def config_ssl_op_legacy_server_connect(self):
        ctx = create_urllib3_context()
        ctx.load_default_certs()
        ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT
        return ctx

    def consult_process(self):
        for index, degree_court in enumerate(self.degrees_court):
            self.court = degree_court.ConfigurationRequisition(self.cnj)
            response = self.request.request("GET", self.court.url_request)
            if response.status == 200:
                html = response.data.decode("utf-8")
                # print(html)
                soap = bs.BeautifulSoup(html, "html.parser")
                if "Não existem informações disponíveis para os parâmetros informados." in html:
                    continue
                elif "processoSelecionado" in html:
                    selected_process = soap.find(id="processoSelecionado")["value"]
                    response = self.request.request("GET", self.court.sub_query(selected_process))
                    if response.status == 200:
                        html = response.data.decode("utf-8")
                extraction = soup_web.Extraction(html)
                extraction.load()
                key_result = self.court.state + " " + self.court.degree
                self.returned_processes.append(extraction.process)
                self.results[key_result] = extraction.process.json()
        return self.results
