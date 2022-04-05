from flask import Blueprint
from app.Controllers import vacinas_controllers


bp = Blueprint("vacinas", __name__, url_prefix="/vaccinations")


bp.get("")(vacinas_controllers.get_all_vaccinations)
bp.get("/<cpf>")(vacinas_controllers.get_one_vaccinations)
bp.get("/nome/<nome>")(vacinas_controllers.get_one_vaccinations_name)
bp.post("")(vacinas_controllers.create_vaccinations)