from flask import Flask
from app.Routes.vacinas_routes import bp as bp_vacinas


def init_app(app: Flask):
    app.register_blueprint(bp_vacinas)
    