import requests
from court import alagoas_first_degree, alagoas_second_degree, ceara_first_degree
from web import extraction
import bs4 as bs


session = requests.Session()
#cnj = "0710802-55.2018.8.02.0001"
# https://esaj.tjce.jus.br/cpopg/open.do
cnj = "0070337-91.2008.8.06.0001"
court = ceara_first_degree.ConfigurationRequisition(cnj)

response = session.get(court.url_request)
if response.status_code == 200:
    html = response.text
    if "processoSelecionado" in html:
        soap = bs.BeautifulSoup(html, "html.parser")
        selected_process = soap.find(id="processoSelecionado")["value"]
        response = session.get(court.sub_query(selected_process))
        if response.status_code == 200:
            html = response.text
    extraction = extraction.Extraction(html)
    extraction.load()
    extraction.process.__str__()