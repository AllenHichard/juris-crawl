import requests
import json


class Requisitions:

    def __init__(self):
        self.session = requests.Session()
        self.headers = {"Content-Type": "application/json"}
        self.payload = {"cnj": "0710802-55.2018.8.02.0001"}
        self.api_local = "http://127.0.0.1:5000/api/consult"
        self.api_cloud = "https://crawler-jus.azurewebsites.net/api/consult"

    def post(self):
        print(requests.post(self.api_cloud, headers=self.headers, data=json.dumps(self.payload)))

    def get(self):
        print(requests.get(self.api_cloud + "/" + self.payload["cnj"]))


r = Requisitions()
r.post()
r.get()