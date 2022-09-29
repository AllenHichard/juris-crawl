import requests
from court import dict_courts
from web import extraction as soup_web
import bs4 as bs


class Session:

    def __init__(self, cnj):
        self.court = None
        self.session = requests.Session()
        self.cnj = cnj.replace(".", "").replace("-", "")
        self.type_court = self.cnj[14:16]
        self.degrees_court = dict_courts[self.type_court]

    def consult_process(self):
        for degree in self.degrees_court:
            self.court = degree.ConfigurationRequisition(self.cnj)
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
                return extraction.process
