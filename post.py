import requests
import json

session = requests.Session()

headers = {
    "Content-Type": "application/json"
}
payload = {
    "cnj" : "0710802-55.2018.8.02.0001"
}


def consulta_post():
    print(requests.post("http://127.0.0.1:5000/api/consult", headers=headers, data=json.dumps(payload)).text)

consulta_post()