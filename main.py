from web import session
from flask import Response
from server import instance
import json

app = instance.app


@app.route("/api", methods=["GET"])
def connected_api():
    return {"status": "browser successfully connected"}


@app.route("/api/consult/<cnj>", methods=["GET"])
def consult_process(cnj):
    s = session.Session(cnj=cnj)
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")


instance.run()
