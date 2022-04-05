from flask import Flask
from environs import Env
from app.Configs import database, migrations
from os import getenv
from app import Routes


env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("APP_CONFIG")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migrations.init_app(app)

    Routes.init_app(app)

    return app