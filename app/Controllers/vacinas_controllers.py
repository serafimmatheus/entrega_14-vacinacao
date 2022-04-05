from http import HTTPStatus
from flask import jsonify, request, current_app
from app.Models.vacinas_models import CardVacinas
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound


def create_vaccinations():
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

    try:
        vaccinations = CardVacinas(**new_data)

        current_app.db.session.add(vaccinations)
        current_app.db.session.commit()

        return {
            "cpf": vaccinations.cpf,
            "name": vaccinations.name,
            "first_shot_date": vaccinations.first_shot_date,
            "second_shot_date": vaccinations.second_shot_date,
            "vaccine_name": vaccinations.vaccine_name,
            "health_unit_name": vaccinations.health_unit_name
        }, HTTPStatus.CREATED

    except IntegrityError as e:
        text = str(e).split("cpf")[1].split("already")[0].replace("(", "").replace(")", "").replace(" ", "").replace("=", "")
        return {"error": f"{text} already exists!"}, HTTPStatus.CONFLICT
    except TypeError as e:
        return {"error": f"{e}"}, HTTPStatus.CONFLICT


def get_all_vaccinations():
    vaccinations = (
        CardVacinas
        .query
        .all()
    )

    serializer = [
        {
            "cpf": vaccination.cpf,
            "name": vaccination.name,
            "first_shot_date": vaccination.first_shot_date,
            "second_shot_date": vaccination.second_shot_date,
            "vaccine_name": vaccination.vaccine_name,
            "health_unit_name": vaccination.health_unit_name
        } for vaccination in vaccinations
    ]

    return jsonify(serializer), HTTPStatus.OK


def get_one_vaccinations(cpf):
    try:
        vaccinations = (
            CardVacinas
            .query
            .get_or_404(cpf, description=f"{cpf} not found!")
        )

        return {
            "cpf": vaccinations.cpf,
            "name": vaccinations.name,
            "first_shot_date": vaccinations.first_shot_date,
            "second_shot_date": vaccinations.second_shot_date,
            "vaccine_name": vaccinations.vaccine_name,
            "health_unit_name": vaccinations.health_unit_name
        }, HTTPStatus.OK
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

        return {
            "cpf": vaccinations.cpf,
            "name": vaccinations.name,
            "first_shot_date": vaccinations.first_shot_date,
            "second_shot_date": vaccinations.second_shot_date,
            "vaccine_name": vaccinations.vaccine_name,
            "health_unit_name": vaccinations.health_unit_name
        }, HTTPStatus.OK
    except NotFound:
        return {"error": f"{nome} not found!"}, HTTPStatus.BAD_REQUEST


    