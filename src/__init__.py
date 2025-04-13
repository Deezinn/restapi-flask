from flask import Flask
from flask_restful import Api
from .db import init_db

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)
    init_db(app)

    return app, api  # <-- Retorna o app e a api
