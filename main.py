from web import session as session
from flask import Flask, Response
import json
import requests

import os
#os.environ['no_proxy'] = '*'

app = Flask(__name__)


@app.route("/", methods=["GET"])
def default():
    session = requests.Session()
    session.trust_env = False
    r = session.get("https://www2.tjal.jus.br/cpopg/open.do")
    return {"Status": "access the api route"}


@app.route("/api", methods=["GET"])
def connected_api():
    a = dict(os.environ["PORT"])
    return {"Status": "browser successfully connected" + str(a)}


@app.route("/api/consult/<cnj>", methods=["GET"])
def consult_process(cnj):
    s = session.Session(cnj=cnj)
    if len(s.cnj) == 20:
        s.consult_process()
        return Response(response=json.dumps(s.results), status=200, mimetype="application/json")
    else:
        return Response(response=json.dumps({"Status": "cnj incorreto"}), status=200, mimetype="application/json")


if __name__ == "__main__":
    a = int(dict(os.environ)['PORT'])
    app.run(port=a, debug=True)
