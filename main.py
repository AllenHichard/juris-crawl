from flask import Flask
from web import session




app = Flask(__name__)

@app.route("/", methods=["GET"])
def connected_api():
    return {"status": "browser successfully connected"}

@app.route("/consult", methods=["GET"])
def consult_process():
    s = session.Session("0070337-91.2008.8.06.0001")  # TJCE
    result = s.consult_process()
    return result.json()

app.run(debug=True)


    #suarios_objetos = Usuario.query.all()
    #usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]

    #return gera_response(200, "usuarios", usuarios_json)


# def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
#     body = {}
#     body[nome_do_conteudo] = conteudo
#
#     if(mensagem):
#         body["mensagem"] = mensagem
#
#     return Response(json.dumps(body), status=status, mimetype="application/json")

# s = session.Session("0070337-91.2008.8.06.0001") #TJCE
# s.consult_process()
# s = session.Session("0710802-55.2018.8.02.0001") # TJAL
# s.consult_process()