from typing import Dict

from src import db
from src.model.i_dto import IDto


class Category(db.Model, IDto):
    def put_into_dto(self) -> Dict[str, object]:
        return {
            "name": self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return Category(
            name=dto_dict.get("name")
        )

    def __init__(self, name):
        self.name = name

    name = db.Column(db.String(45), primary_key=True)
