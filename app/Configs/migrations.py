from flask import Flask
from flask_migrate import Migrate
from app.Configs.database import db


def init_app(app: Flask):
    Migrate(app, db, compare_type=True)
    