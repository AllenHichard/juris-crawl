import requests
from court import dict_courts
from web import extraction as soup_web
import bs4 as bs
import urllib3
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
        self.cnj = cnj.replace(".", "").replace("-", "")
        print(self.cnj)
        self.type_court = self.cnj[14:16]
        self.degrees_court = dict_courts[self.type_court]
        self.results = dict()

    def consult_process(self):
        for degree_court in self.degrees_court:
            self.court = degree_court.ConfigurationRequisition(self.cnj)
            response = self.session.get(self.court.url_request)
            if response.status_code == 200:
                html = response.text
                if "processoSelecionado" in html:
                    soap = bs.BeautifulSoup(html, "html.parser")
                    selected_process = soap.find(id="processoSelecionado")["value"]
                    response = self.session.get(self.court.sub_query(selected_process))
                    if response.status_code == 200:
                        html = response.text
                extraction = soup_web.Extraction(html)
                extraction.load()
                key_result = self.court.state + " " + self.court.degree
                self.results[key_result] = extraction.process.json()
        return self.results
