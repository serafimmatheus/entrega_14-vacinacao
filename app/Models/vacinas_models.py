from sqlalchemy import Column, String, DateTime, CheckConstraint
from app.Configs.database import db
from dataclasses import dataclass


@dataclass
class CardVacinas(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str


    __tablename__ = "vaccine_cards"
    __table_args__ = (CheckConstraint("cpf ~ '[0-9]{11}'"),)

    cpf = Column(String(11), primary_key=True, unique=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime) 
    second_shot_date = Column(DateTime) 
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

