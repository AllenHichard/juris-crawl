from web import session
from flask import Flask, Response
import json


app = Flask(__name__)


@app.route("/", methods=["GET"])
def default():
    return {"status": "access the api route"}


@app.route("/api", methods=["GET"])
def connected_api():
    return {"status": "browser successfully connected"}


@app.route("/api/consult/<cnj>", methods=["GET"])
def consult_process(cnj):
    s = session.Session(cnj=cnj)
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run()

#UNSAFE_LEGACY_RENEGOTIATION_DISABLED - Heroku