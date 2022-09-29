from flask import Flask, Response
from web import session
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def connected_api():
    return {"status": "browser successfully connected"}


@app.route("/consult/<cnj>", methods=["GET"])
def consult_process(cnj):
    s = session.Session(cnj=cnj)  # TJCE
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")


app.run(debug=True)
