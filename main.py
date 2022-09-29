from web import session
from flask import Flask, Response
import json


app = Flask(__name__)


@app.route("/", methods=["GET"])
def default():
    #return {"status": "access the api route"}
    s = session.Session(cnj="0710802-55.2018.8.02.0001")
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")


@app.route("/api", methods=["GET"])
def connected_api():
    return {"status": "browser successfully connected"}


@app.route("/api/consult/<cnj>", methods=["GET"])
def consult_process(cnj):
    s = session.Session(cnj=cnj)
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)

#UNSAFE_LEGACY_RENEGOTIATION_DISABLED - Heroku
#https://stackoverflow.com/questions/71603314/ssl-error-unsafe-legacy-renegotiation-disabled