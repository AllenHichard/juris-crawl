import requests
from court import dict_courts
from web import extraction as soup_web
import bs4 as bs

import urllib3
from urllib3.util.ssl_ import create_urllib3_context
import ssl


class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)

# ctx = create_urllib3_context()
# ctx.load_default_certs()
# ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session



class Session:

    def __init__(self, cnj):
        self.court = None
        self.session = get_legacy_session()
        #self.session = urllib3.PoolManager(ssl_context=ctx)
        self.cnj = cnj.replace(".", "").replace("-", "")
        self.type_court = self.cnj[14:16]
        self.degrees_court = dict_courts[self.type_court]
        self.returned_processes = []
        self.results = dict()

    def consult_process(self):
        for index, degree_court in enumerate(self.degrees_court):
            self.court = degree_court.ConfigurationRequisition(self.cnj)
            response = self.session.request("GET", self.court.url_request)
            if response.status_code == 200:
                html = response.text#response.data.decode("utf-8")
                #print(html)
                soap = bs.BeautifulSoup(html, "html.parser")
                if "Não existem informações disponíveis para os parâmetros informados." in html:
                    continue
                elif "processoSelecionado" in html:
                    selected_process = soap.find(id="processoSelecionado")["value"]
                    response = self.session.request("GET", self.court.sub_query(selected_process))
                    if response.status_code == 200:
                        html = response.text#response.data.decode("utf-8")
                extraction = soup_web.Extraction(html)
                extraction.load()
                key_result = self.court.state + " " + self.court.degree
                self.returned_processes.append(extraction.process)
                self.results[key_result] = extraction.process.json()
        return self.results
