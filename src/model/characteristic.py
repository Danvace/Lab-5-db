from typing import Dict

from src import db
from src.model.i_dto import IDto


class Characteristic(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    def __init__(self, width, length, weight):
        self.width = width
        self.length = length
        self.weight = weight

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "width": self.width,
            "length": self.length,
            "weight": self.weight
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        characteristic = Characteristic(
            width=dto_dict.get("width"),
            length=dto_dict.get("length"),
            weight=dto_dict.get("weight")
        )
        return characteristic
