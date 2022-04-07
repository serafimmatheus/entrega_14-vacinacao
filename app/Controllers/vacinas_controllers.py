from http import HTTPStatus
from flask import jsonify, request, current_app
from app.Models.vacinas_models import CardVacinas
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import DataError
from werkzeug.exceptions import BadRequest



def create_vaccinations():

    try:
        data = request.get_json()

        today_date = datetime.today()
        td = timedelta(90)

        new_data = {
            "cpf": data["cpf"],
            "name": data["name"].title(),
            "first_shot_date": today_date,
            "second_shot_date": today_date + td,
            "vaccine_name": data["vaccine_name"],
            "health_unit_name": data["health_unit_name"].capitalize()
        }

        vaccinations = CardVacinas(**new_data)

        current_app.db.session.add(vaccinations)
        current_app.db.session.commit()

        return jsonify(vaccinations), HTTPStatus.CREATED

    except IntegrityError as e:
        text = str(e).split("cpf")[1].split("already")[0].replace("(", "").replace(")", "").replace(" ", "").replace("=", "")
        return {"error": f"{text} already exists!"}, HTTPStatus.CONFLICT
    except TypeError as e:
        return {"error": f"{e}"}, HTTPStatus.CONFLICT
    except KeyError as e:
        return {"error": f"{e}"}, HTTPStatus.BAD_REQUEST
    except AttributeError as e:
        return {"error": f"{e}"}, HTTPStatus.BAD_REQUEST
    except (DataError, BadRequest):
        return {"error": {
            "cpf": "str of numbers max(11)",
            "name": "str",
            "vaccine_name": "str",
            "health_unit_name": "str"
        }}, HTTPStatus.BAD_REQUEST

def get_all_vaccinations():
    vaccinations = (
        CardVacinas
        .query
        .all()
    )

    return jsonify(vaccinations), HTTPStatus.OK


def get_one_vaccinations(cpf):
    try:
        vaccinations = (
            CardVacinas
            .query
            .get_or_404(cpf, description=f"{cpf} not found!")
        )

        return jsonify(vaccinations), HTTPStatus.OK
    except NotFound as e:
        return {"error": f"{cpf} not found!"}, HTTPStatus.BAD_REQUEST

def get_one_vaccinations_name(nome):
    try:
        vaccinations = (
            CardVacinas
            .query
            .filter_by(name=nome)
            .first()
        )

        return jsonify(vaccinations), HTTPStatus.OK
    except NotFound:
        return {"error": f"{nome} not found!"}, HTTPStatus.BAD_REQUEST


    