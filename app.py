from web import session as session
from flask import Flask, Response, request
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
def get_consult_process(cnj):
    s = session.Session(cnj=cnj)
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")

@app.route("/api/consult", methods=["POST"])
def post_consult_process():
    body = request.get_json()
    s = session.Session(cnj=body["cnj"])
    s.consult_process()
    return Response(response=json.dumps(s.results), status=200, mimetype="application/json")



if __name__ == "__main__":
    app.run(debug=True)
