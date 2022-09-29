import requests

from court import dict_courts
from web import extraction as soup_web
import bs4 as bs



class Session:

    def __init__(self, cnj):
        self.court = None
        self.request = requests.Session()
        self.cnj = cnj.replace(".", "").replace("-", "")
        self.type_court = self.cnj[14:16]
        self.degrees_court = dict_courts[self.type_court]
        self.returned_processes = []
        self.results = dict()

    def consult_process(self):
        for index, degree_court in enumerate(self.degrees_court):
            self.court = degree_court.ConfigurationRequisition(self.cnj)
            response = self.request.get(self.court.url_request)
            if response.status_code == 200:
                html = response.text
                # print(html)
                soap = bs.BeautifulSoup(html, "html.parser")
                if "Não existem informações disponíveis para os parâmetros informados." in html:
                    continue
                elif "processoSelecionado" in html:
                    selected_process = soap.find(id="processoSelecionado")["value"]
                    response = self.request.get(self.court.sub_query(selected_process))
                    if response.status_code == 200:
                        html = response.text
                extraction = soup_web.Extraction(html)
                extraction.load()
                key_result = self.court.state + " " + self.court.degree
                self.returned_processes.append(extraction.process)
                self.results[key_result] = extraction.process.json()
        return self.results
