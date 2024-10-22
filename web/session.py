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
        self.returned_processes = []
        self.results = dict()

    def config_ssl_op_legacy_server_connect(self):
        ctx = create_urllib3_context()
        ctx.load_default_certs()
        ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT
        return ctx

    def validate_cnj(self):
        if self.type_court not in dict_courts or len(self.cnj) != 20:
            self.results = {"Status": "cnj incorreto"}
            return False
        return True

    def consult_process(self):
        if self.validate_cnj():
            return self.consult_validated_process(dict_courts[self.type_court])
        else:
            return self.results

    def change_query_route(self, html):
        soap = bs.BeautifulSoup(html, "html.parser")
        if "processoSelecionado" in html:
            selected_process = soap.find(id="processoSelecionado")["value"]
            response = self.request.request("GET", self.court.sub_query(selected_process))
            html = response.data.decode("utf-8")
        return html

    def consult_validated_process(self, degrees_court):
        for index, degree_court in enumerate(degrees_court):
            self.court = degree_court.ConfigurationRequisition(self.cnj)
            key_result = self.court.state + " " + self.court.degree
            try:
                response = self.request.request("GET", self.court.url_request)
                html = response.data.decode("utf-8")
                html = self.change_query_route(html)
                extraction = soup_web.Extraction(html)
                extraction.load()
                self.returned_processes.append(extraction.process)
                self.results[key_result] = extraction.process.json()
            except:
                self.results[key_result] = {"Status": "Crawler Impedido de Acessar"}
        return self.results
