from web import session as session
from flask import Flask, Response
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def default():
    msg = {"Status": "access the api route"}
    return Response(response=json.dumps(msg), status=200, mimetype="application/json")


@app.route("/api", methods=["GET"])
def connected_api():
    msg = {"Status": "browser successfully connected"}
    return Response(response=json.dumps(msg), status=200, mimetype="application/json")


@app.route("/api/consult/<cnj>", methods=["GET"])
def consult_process(cnj):
    s = session.Session(cnj=cnj)
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
