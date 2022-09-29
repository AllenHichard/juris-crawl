from flask import Flask


class Server:

    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run(
            host='0.0.0.0', port=8080,
            debug=True
        )
