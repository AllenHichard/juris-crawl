from flask import Flask


class Server:

    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run(
            port=8080
        )
